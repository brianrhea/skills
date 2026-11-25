#!/usr/bin/env python3
"""Prepare a research corpus for analysis.

Reads transcripts (.vtt, .srt, .txt, .md) and exports (.csv, .tsv, .json,
.jsonl, .ndjson), and writes a clean, numbered copy that quotes can be checked
against:

  <out>/<doc_id>.md            one file per transcript, one numbered turn per line
  <out>/<source>.items.jsonl   one record per ticket, response or review
  <out>/index.csv              every document, its size and any warnings

It never calls a model. Run it before reading the raw files.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys

TEXT_EXT = {".txt", ".md", ".vtt", ".srt"}
TABLE_EXT = {".csv", ".tsv"}
JSON_EXT = {".json", ".jsonl", ".ndjson"}
ID_NAMES = ("id", "ticket_id", "ticket id", "conversation_id", "response_id", "deal_id", "case_id", "number")
NAME_COLS = ("name", "requester", "customer", "contact", "respondent", "author", "user", "email", "requester_email")
MIN_TEXT = 40  # characters; shorter cells are treated as metadata

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"(?<!\w)(?:\+?\d[\d\s().-]{7,}\d)(?!\w)")
TIMING = re.compile(r"^\d{1,2}:\d{2}(?::\d{2})?[.,]\d{3}\s*-->")
SPEAKER_LINE = re.compile(r"^([A-Z][\w .'’-]{0,40}?)\s*(?:\[[^\]]*\]|\([^)]*\))?\s*:\s+(\S.*)$")
VOICE_TAG = re.compile(r"<v(?:\.[\w.-]+)?\s+([^>]+)>")
TAG = re.compile(r"<[^>]+>")


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "doc"


def clean(text):
    return re.sub(r"\s+", " ", TAG.sub("", text or "")).strip()


def merge_turns(pairs):
    """Join consecutive lines from the same speaker into one turn."""
    turns = []
    for speaker, text in pairs:
        text = clean(text)
        if not text:
            continue
        if turns and turns[-1][0] == speaker:
            turns[-1][1] += " " + text
        else:
            turns.append([speaker, text])
    return turns


def parse_cues(raw):
    """VTT and SRT: drop headers, cue numbers and timings; keep speaker and text."""
    pairs, speaker = [], ""
    for line in raw.splitlines():
        line = line.strip()
        if not line or line == "WEBVTT" or line.startswith(("NOTE", "Kind:", "Language:")) or line.isdigit() or TIMING.match(line):
            continue
        voice = VOICE_TAG.search(line)
        if voice:
            speaker, line = voice.group(1).strip(), TAG.sub("", line)
        else:
            named = SPEAKER_LINE.match(line)
            if named:
                speaker, line = named.group(1).strip(), named.group(2)
        pairs.append((speaker, line))
    return merge_turns(pairs)


def parse_plain(raw):
    """Plain text: use 'Name: words' lines when the file has them, otherwise paragraphs."""
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    labelled = sum(1 for l in lines if SPEAKER_LINE.match(l))
    if lines and labelled / len(lines) >= 0.3:
        pairs, speaker = [], ""
        for line in lines:
            named = SPEAKER_LINE.match(line)
            if named:
                speaker, line = named.group(1).strip(), named.group(2)
            pairs.append((speaker, line))
        return merge_turns(pairs)
    paragraphs = [clean(p) for p in re.split(r"\n\s*\n", raw)]
    return [["", p] for p in paragraphs if p]


def long_strings(value, path=""):
    """Every string of at least MIN_TEXT characters inside a JSON value."""
    if isinstance(value, str):
        text = clean(value)
        if len(text) >= MIN_TEXT:
            yield path, text
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from long_strings(child, f"{path}.{key}" if path else str(key))
    elif isinstance(value, list):
        for child in value:
            yield from long_strings(child, path)


def read_table(path):
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        delimiter = "\t" if path.endswith(".tsv") else ","
        try:
            delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t").delimiter
        except csv.Error:
            pass
        return list(csv.DictReader(handle, delimiter=delimiter))


def read_json(path):
    with open(path, encoding="utf-8-sig", errors="replace") as handle:
        raw = handle.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return [json.loads(line) for line in raw.splitlines() if line.strip()]
    if isinstance(data, list):
        return data
    for value in data.values():
        if isinstance(value, list) and value and isinstance(value[0], dict):
            return value
    return [data]


def find_id(record):
    for key in record:
        if str(key).strip().lower() in ID_NAMES and str(record[key]).strip():
            return str(record[key]).strip()
    return None


class Pseudonyms:
    """Swap speaker names for codes and mask emails and phone numbers."""

    def __init__(self, enabled, interviewers):
        self.enabled = enabled
        self.interviewers = {n.lower() for n in interviewers}
        self.codes = {}

    def is_interviewer(self, speaker):
        low = speaker.lower()
        return any(low == n or low.startswith(n + " ") or n in low.split() for n in self.interviewers)

    def code(self, speaker):
        if not speaker:
            return ""
        if self.is_interviewer(speaker):
            return "Interviewer"
        if not self.enabled:
            return speaker
        if speaker not in self.codes:
            self.codes[speaker] = f"P{len(self.codes) + 1:02d}"
        return self.codes[speaker]

    def scrub(self, text, extra_names=()):
        if not self.enabled:
            return text
        text = EMAIL.sub("[email]", text)
        text = PHONE.sub("[phone]", text)
        for name in list(self.codes) + list(extra_names):
            parts = [name] + [p for p in name.split() if len(p) >= 3]
            for part in sorted(set(parts), key=len, reverse=True):
                replacement = self.codes.get(name, "[name]")
                text = re.sub(rf"\b{re.escape(part)}\b", replacement, text, flags=re.IGNORECASE)
        return text


def main():
    parser = argparse.ArgumentParser(description="Prepare a research corpus so quotes can be verified against it.")
    parser.add_argument("inputs", nargs="+", help="files or folders to read")
    parser.add_argument("--out", default="research/corpus", help="where to write the prepared corpus")
    parser.add_argument("--interviewer", action="append", default=[], help="name of an interviewer, agent or rep; repeat for several")
    parser.add_argument("--codes", action="store_true", help="replace speaker names with P01, P02 and mask emails and phones")
    args = parser.parse_args()

    files = []
    for item in args.inputs:
        if os.path.isdir(item):
            for root, _dirs, names in os.walk(item):
                files += [os.path.join(root, n) for n in sorted(names) if not n.startswith(".")]
        else:
            files.append(item)

    os.makedirs(args.out, exist_ok=True)
    names = Pseudonyms(args.codes, args.interviewer)
    index, seen, used_ids, warnings = [], {}, set(), []

    def unique(doc_id):
        base, n = doc_id, 2
        while doc_id in used_ids:
            doc_id, n = f"{base}-{n}", n + 1
        used_ids.add(doc_id)
        return doc_id

    def register(doc_id, kind, source, text, turns=1):
        digest = hashlib.sha1(re.sub(r"\W+", " ", text.lower()).strip().encode()).hexdigest()
        duplicate_of = seen.get(digest, "")
        seen.setdefault(digest, doc_id)
        index.append({"doc_id": doc_id, "kind": kind, "source": source, "words": len(text.split()), "turns": turns, "duplicate_of": duplicate_of})
        return not duplicate_of

    for path in files:
        ext = os.path.splitext(path)[1].lower()
        source = os.path.basename(path)
        if ext in TEXT_EXT:
            with open(path, encoding="utf-8-sig", errors="replace") as handle:
                raw = handle.read()
            turns = parse_cues(raw) if ext in {".vtt", ".srt"} else parse_plain(raw)
            if not turns:
                warnings.append(f"{source}: no text found")
                continue
            for speaker, _text in turns:
                names.code(speaker)
            doc_id = unique(slug(os.path.splitext(source)[0]))
            lines, body = [], []
            for n, (speaker, text) in enumerate(turns, 1):
                role = "interviewer" if speaker and names.is_interviewer(speaker) else ("customer" if speaker else "unknown")
                text = names.scrub(text)
                body.append(text)
                lines.append(f"[T{n:03d}] {names.code(speaker) or 'Unknown'} ({role}): {text}")
            if register(doc_id, "transcript", source, " ".join(body), len(turns)):
                with open(os.path.join(args.out, doc_id + ".md"), "w", encoding="utf-8") as handle:
                    handle.write(f"# {doc_id}\nSource: {path}\n\n" + "\n".join(lines) + "\n")
            if args.interviewer and not any("(interviewer)" in l for l in lines):
                warnings.append(f"{source}: no turns matched the interviewer name given")
            if not any(s for s, _t in turns):
                warnings.append(f"{source}: no speaker labels, so customer and interviewer speech cannot be told apart")
        elif ext in TABLE_EXT or ext in JSON_EXT:
            try:
                records = read_table(path) if ext in TABLE_EXT else read_json(path)
            except (OSError, ValueError) as error:
                warnings.append(f"{source}: could not be read ({error})")
                continue
            base = slug(os.path.splitext(source)[0])
            kept, with_text = [], 0
            for n, record in enumerate(records, 1):
                if not isinstance(record, dict):
                    continue
                parts = list(long_strings(record))
                meta = {str(k): str(v)[:80] for k, v in record.items() if isinstance(v, (str, int, float)) and len(str(v)) < MIN_TEXT and str(v).strip()}
                people = [str(record[k]) for k in record if str(k).strip().lower() in NAME_COLS and isinstance(record[k], str) and record[k].strip()]
                if args.codes:
                    meta = {k: v for k, v in meta.items() if k.strip().lower() not in NAME_COLS}
                text = names.scrub("\n".join(t for _p, t in parts), people)
                doc_id = unique(f"{base}-{find_id(record) or n}")
                if text:
                    with_text += 1
                if text and register(doc_id, "item", source, text):
                    kept.append({"doc_id": doc_id, "text": text, "meta": meta})
            if records and not with_text:
                warnings.append(f"{source}: {len(records)} rows but no customer text. This looks like a metadata-only export; get the export that includes message bodies or comments.")
            elif kept:
                with open(os.path.join(args.out, base + ".items.jsonl"), "w", encoding="utf-8") as handle:
                    for row in kept:
                        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        else:
            warnings.append(f"{source}: file type {ext or '(none)'} is not supported; convert it to text, CSV or JSON")

    with open(os.path.join(args.out, "index.csv"), "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["doc_id", "kind", "source", "words", "turns", "duplicate_of"])
        writer.writeheader()
        writer.writerows(index)
    if names.codes:
        with open(os.path.join(args.out, "participants.key.csv"), "w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["code", "name"])
            writer.writerows((code, name) for name, code in names.codes.items())

    originals = [row for row in index if not row["duplicate_of"]]
    words = sum(row["words"] for row in originals)
    transcripts = sum(1 for row in originals if row["kind"] == "transcript")
    items = len(originals) - transcripts
    if transcripts > 50 or items > 2000:
        tier = "large: start with a sample, fix the themes, then process everything one document at a time"
    elif transcripts > 10 or items > 300:
        tier = "medium: process one document or small batch at a time, writing to disk"
    else:
        tier = "small: can be read directly"
    print(f"Prepared {len(originals)} documents ({transcripts} transcripts, {items} items), about {words:,} words (~{int(words * 1.35):,} tokens).")
    print(f"Duplicates set aside: {len(index) - len(originals)}")
    print(f"Scale: {tier}")
    print(f"Written to: {args.out}")
    for warning in warnings:
        print("WARNING: " + warning)
    if not originals:
        sys.exit("Nothing usable was found.")


if __name__ == "__main__":
    main()
