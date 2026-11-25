#!/usr/bin/env python3
"""Count how many documents support each theme, from verified evidence only.

Counts distinct documents, so one person raising a point five times counts
once. The denominator is the number of documents in the corpus index, not the
number that happened to mention something.
"""
import argparse
import csv
import json
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="Count documents per theme from a verified evidence file.")
    parser.add_argument("evidence", help="the .verified.jsonl file written by verify_quotes.py")
    parser.add_argument("--by", default="theme", help="field to count by; may hold one value or a list (default: theme)")
    parser.add_argument("--corpus", default="research/corpus", help="folder written by prepare.py")
    parser.add_argument("--split", help="optional second field to break each count down by, such as source or segment")
    args = parser.parse_args()

    total = 0
    index_path = os.path.join(args.corpus, "index.csv")
    if os.path.exists(index_path):
        with open(index_path, newline="", encoding="utf-8") as handle:
            total = sum(1 for row in csv.DictReader(handle) if not row.get("duplicate_of"))

    groups, skipped, analysed = {}, 0, set()
    with open(args.evidence, encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("status") != "verified":
                skipped += 1
                continue
            analysed.add(record["doc_id"])
            values = record.get(args.by) or ["(none)"]
            values = values if isinstance(values, list) else [values]
            split = str(record.get(args.split, "(none)")) if args.split else ""
            for value in values:
                group = groups.setdefault((str(value), split), {"docs": set(), "quotes": 0})
                group["docs"].add(record["doc_id"])
                group["quotes"] += 1

    if not groups:
        sys.exit("No verified evidence to count. Run verify_quotes.py first.")
    total = total or len(analysed)
    fields = [args.by] + ([args.split] if args.split else []) + ["documents", "of", "share", "quotes", "examples"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fields)
    writer.writeheader()
    for (value, split), group in sorted(groups.items(), key=lambda item: (-len(item[1]["docs"]), item[0])):
        row = {args.by: value, "documents": len(group["docs"]), "of": total, "share": f"{100 * len(group['docs']) / total:.0f}%",
               "quotes": group["quotes"], "examples": " ".join(sorted(group["docs"])[:3])}
        if args.split:
            row[args.split] = split
        writer.writerow(row)
    print(f"{len(analysed)} of {total} documents have verified evidence.", file=sys.stderr)
    if skipped:
        print(f"{skipped} unverified records were left out of the counts.", file=sys.stderr)


if __name__ == "__main__":
    main()
