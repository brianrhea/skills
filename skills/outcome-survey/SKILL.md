---
name: outcome-survey
description: Turn Jobs to Be Done outcome statements into an importance and satisfaction survey, and score the responses to rank unmet customer needs. Use when the user wants to prioritize a roadmap with a JTBD survey, quantify interview findings, or analyze importance/satisfaction survey results.
---

# Outcome Survey

Interviews tell you which needs exist. A survey tells you which ones matter to the most people. This skill has two modes: writing the survey and scoring the results. Choose the mode from what the user has: a response export means scoring, and anything else means writing.

## Setup: none required

The user should never have to create folders, rename files or run another skill first.

- **Input.** For writing, the outcome statements in `research/job-map.md`, or any list of outcomes the user pastes or points to. If there is no job map, build one first by following the job-map skill. For scoring, the response export from the user's survey tool, wherever it was downloaded.
- **Workspace.** Save output in a `research/` folder in the current project, creating it if it does not exist. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. If you need the product, the buyer or the decision being studied and the file does not have them, ask once and save the answers there.
- **Finish.** Reply with a short summary of what you found, where it was saved, and the one next step you recommend. Offer to do that step.

## Mode 1: write the survey

For each outcome, write a pair of questions on the same five-point scale:

- "How important is it to you to <outcome>?" Not at all, Slightly, Moderately, Very, Extremely.
- "How satisfied are you with your ability to <outcome> today?" Same five labels.

Rules:

- Rewrite each outcome into plain second-person language, keeping the meaning. "Minimize the time it takes to reconcile figures" becomes "reconcile figures from different sources quickly".
- Keep the outcome's number as the question ID (`O1`, `O2`) so results map back to the job map.
- Above about 40 outcomes, tell the user the survey is too long and propose which steps to cut or split across respondents.
- Open with three or four screening and segmentation questions: role, company size, current solution.
- Close with one open question: "What is the hardest part of <job>?"

Write to `research/survey/survey.md` in a layout that pastes cleanly into a survey tool, and write `research/survey/outcomes.csv` with columns `id,step,outcome`.

## Mode 2: score the results

Input is the response export as CSV. Ask which columns hold importance and satisfaction for each outcome if the header does not make it obvious.

Run `scripts/score.py` from this skill's folder. Do not compute scores by hand.

```bash
python3 <this skill's folder>/scripts/score.py <responses.csv> --outcomes research/survey/outcomes.csv
```

The script expects columns named `<id>_importance` and `<id>_satisfaction`, holding either the numbers 1 to 5 or the scale labels. If the export is shaped differently, reshape it into that layout first and tell the user what you changed.

### How scores are calculated

- **Importance** is the share of respondents answering Very or Extremely, scaled to 0 to 10. If 82% chose the top two, importance is 8.2.
- **Satisfaction** is calculated the same way.
- **Opportunity** = importance + max(importance − satisfaction, 0).

| Result | Meaning |
| --- | --- |
| High importance, low satisfaction | Underserved. Build here. |
| High importance, high satisfaction | Table stakes. Match it. |
| Low importance, high satisfaction | Overserved. Room for something simpler or cheaper. |
| Low importance, low satisfaction | Leave it alone. |

### Reporting

Write `research/survey/results.md` with:

- The number of responses, and a warning above the table if it is under 30.
- All outcomes ranked by opportunity, with importance, satisfaction and job-map step.
- The underserved and overserved lists.
- Which job-map steps hold the most opportunity.
- Differences between segments, only where each segment has at least 30 responses.

Report what the numbers say. Recommendations about what to build belong to the user.
