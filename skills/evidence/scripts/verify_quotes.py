#!/usr/bin/env python3
"""Check that every quote in an evidence file exists in the prepared corpus.

Each line of the evidence file is a JSON record with at least "doc_id" and
"quote". A quote passes when its words appear, in order, in something a
customer said in that document. Use "..." where words are left out.

Statuses written to <evidence>.verified.jsonl:
  verified      found word for word in customer speech
  altered       not found, but close to a real passage (given as "closest")
  interviewer   found only in the interviewer's or agent's speech
  not_found     nothing close in that document
  unknown_doc   the doc_id is not in the corpus

Exits with status 1 if any quote is not verified.
"""
import argparse
import difflib
import glob
import json
import os
import re
import sys
import unicodedata

TURN = re.compile(r"^\[(T\d+)\] .*? \((customer|interviewer|unknown)\): (.*)$")
GAP = re.compile(r"\s*(?:\[\s*(?:\.\.\.|…)\s*\]|\.\.\.|…)\s*")
SWAPS = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", " ": " "})


def norm(text):
    text = unicodedata.normalize("NFKC", text or "").translate(SWAPS).lower()
    return re.sub(r"\s+", " ", text).strip()


def load_corpus(folder):
    """doc_id -> list of (turn_id, role, normalised text, original text)."""
    docs = {}
    for path in glob.glob(os.path.join(folder, "*.md")):
        turns = []
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                match = TURN.match(line.rstrip("\n"))
                if match:
                    turns.append((match.group(1), match.group(2), norm(match.group(3)), match.group(3)))
        docs[os.path.splitext(os.path.basename(path))[0]] = turns
    for path in glob.glob(os.path.join(folder, "*.items.jsonl")):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    docs[row["doc_id"]] = [("T001", "customer", norm(row["text"]), row["text"])]
    return docs


def find_in_order(segments, turns, roles):
    """Turn ids where each segment appears, in order, among turns with these roles."""
    hits, turn_index, offset = [], 0, 0
    for segment in segments:
        found = False
        while turn_index < len(turns):
            turn_id, role, text, _original = turns[turn_index]
            position = text.find(segment, offset) if role in roles else -1
            if position >= 0:
                hits.append(turn_id)
                offset, found = position + len(segment), True
                break
            turn_index, offset = turn_index + 1, 0
        if not found:
            return None
    return hits


def closest(quote, turns):
    best, best_score = None, 0.0
    for turn_id, role, text, original in turns:
        if role == "interviewer":
            continue
        blocks = difflib.SequenceMatcher(None, quote, text, autojunk=False).get_matching_blocks()
        matched = sum(b.size for b in blocks if b.size >= 4)
        score = matched / max(len(quote), 1)
        if score > best_score:
            usable = [b for b in blocks if b.size >= 4]
            start = usable[0].b if usable else 0
            end = usable[-1].b + usable[-1].size if usable else 0
            snippet = re.sub(r"\s+", " ", original).strip()
            best, best_score = {"turn": turn_id, "text": snippet if len(snippet) < 400 else text[start:end]}, score
    return best, best_score


def main():
    parser = argparse.ArgumentParser(description="Verify quotes against the prepared corpus.")
    parser.add_argument("evidence", help="JSONL file of evidence records")
    parser.add_argument("--corpus", default="research/corpus", help="folder written by prepare.py")
    args = parser.parse_args()

    docs = load_corpus(args.corpus)
    if not docs:
        sys.exit(f"No prepared documents in {args.corpus}. Run prepare.py first.")

    records, counts = [], {}
    with open(args.evidence, encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                sys.exit(f"Line {number} of {args.evidence} is not valid JSON.")
            quote = norm(str(record.get("quote", ""))).strip("\"' ")
            segments = [s for s in GAP.split(quote) if s]
            turns = docs.get(str(record.get("doc_id", "")))
            record.pop("closest", None)
            if turns is None:
                status = "unknown_doc"
            elif not segments:
                status = "not_found"
            else:
                has_roles = any(role != "unknown" for _t, role, _n, _o in turns)
                customer = ("customer", "unknown") if has_roles else ("unknown", "customer")
                hits = find_in_order(segments, turns, customer)
                if hits:
                    status, record["turn"] = "verified", hits[0]
                elif find_in_order(segments, turns, ("interviewer",)):
                    status = "interviewer"
                else:
                    match, score = closest(quote, turns)
                    if match and score >= 0.8:
                        status, record["closest"] = "altered", match
                    else:
                        status = "not_found"
            record["status"] = status
            counts[status] = counts.get(status, 0) + 1
            records.append(record)

    out = re.sub(r"(\.verified)?\.jsonl$", "", args.evidence) + ".verified.jsonl"
    with open(out, "w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    total = len(records)
    print(f"{counts.get('verified', 0)} of {total} quotes verified. Written to {out}")
    for status in ("altered", "interviewer", "not_found", "unknown_doc"):
        if counts.get(status):
            print(f"  {status}: {counts[status]}")
    for record in records:
        if record["status"] != "verified":
            print(f"  - [{record['status']}] {record.get('doc_id')}: {str(record.get('quote'))[:90]}")
    if counts.get("verified", 0) != total:
        sys.exit(1)


if __name__ == "__main__":
    main()
