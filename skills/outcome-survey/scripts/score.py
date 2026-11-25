#!/usr/bin/env python3
"""Score an importance/satisfaction outcome survey.

Reads a CSV with one row per respondent and, for every outcome, two columns
named <id>_importance and <id>_satisfaction. Values are 1-5 or the labels
Not at all / Slightly / Moderately / Very / Extremely.

Importance and satisfaction are the share of respondents answering 4 or 5,
scaled to 0-10. Opportunity = importance + max(importance - satisfaction, 0).
"""
import argparse
import csv
import sys

LABELS = {"not at all": 1, "slightly": 2, "moderately": 3, "very": 4, "extremely": 5}


def to_score(value):
    """Return 1-5 for a response cell, or None when it is blank or unreadable."""
    text = (value or "").strip().lower()
    if not text:
        return None
    if text in LABELS:
        return LABELS[text]
    for label, score in LABELS.items():
        if text.startswith(label):
            return score
    try:
        number = int(float(text))
    except ValueError:
        return None
    return number if 1 <= number <= 5 else None


def top_two(values):
    """Share of answers that are 4 or 5, on a 0-10 scale."""
    answered = [v for v in values if v is not None]
    if not answered:
        return None, 0
    return 10 * sum(1 for v in answered if v >= 4) / len(answered), len(answered)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("responses", help="CSV export of survey responses")
    parser.add_argument("--outcomes", help="CSV with columns id,step,outcome")
    args = parser.parse_args()

    with open(args.responses, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        sys.exit("No responses found in " + args.responses)

    lookup = {name.strip().lower(): name for name in rows[0]}
    ids = sorted(
        name[: -len("_importance")]
        for name in lookup
        if name.endswith("_importance") and name[: -len("_importance")] + "_satisfaction" in lookup
    )
    if not ids:
        sys.exit("No <id>_importance / <id>_satisfaction column pairs found.")

    details = {}
    if args.outcomes:
        with open(args.outcomes, newline="", encoding="utf-8-sig") as handle:
            for row in csv.DictReader(handle):
                details[row["id"].strip().lower()] = row

    results = []
    for outcome_id in ids:
        importance, n_imp = top_two([to_score(r[lookup[outcome_id + "_importance"]]) for r in rows])
        satisfaction, n_sat = top_two([to_score(r[lookup[outcome_id + "_satisfaction"]]) for r in rows])
        if importance is None or satisfaction is None:
            continue
        opportunity = importance + max(importance - satisfaction, 0)
        info = details.get(outcome_id, {})
        results.append(
            {
                "id": outcome_id.upper(),
                "step": info.get("step", ""),
                "outcome": info.get("outcome", ""),
                "importance": round(importance, 1),
                "satisfaction": round(satisfaction, 1),
                "opportunity": round(opportunity, 1),
                "responses": min(n_imp, n_sat),
            }
        )

    results.sort(key=lambda r: r["opportunity"], reverse=True)
    writer = csv.DictWriter(sys.stdout, fieldnames=list(results[0]))
    writer.writeheader()
    writer.writerows(results)
    print(f"{len(rows)} respondents, {len(results)} outcomes scored", file=sys.stderr)
    if len(rows) < 30:
        print("Warning: fewer than 30 responses; treat the ranking as directional.", file=sys.stderr)


if __name__ == "__main__":
    main()
