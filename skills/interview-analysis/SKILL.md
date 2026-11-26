---
name: interview-analysis
description: Analyze a customer interview transcript with Jobs to Be Done, extracting the buying timeline, struggling moments and Forces of Progress with verbatim quotes. Use when the user shares or points to interview transcripts, call recordings as text, or asks what a customer said.
---

# Interview Analysis

Turn one transcript into a one-page summary that a person who was not on the call can trust. Handle one interview at a time. When given a folder or several files, repeat the process for each and write one summary per interview.

## Setup: none required

The user should never have to create folders, rename files or run another skill first.

- **Input.** Use whatever the user points to: a file, a folder, pasted text, an attachment, or a link you can open with a connected tool. Leave their files where they are. If they point to nothing, look in the current folder for files that read like interview transcripts, list what you found, and confirm before analyzing. When a transcript is pasted or attached and exists nowhere on disk, save it unchanged to `research/transcripts/<name>.md` so its quotes can be checked later.
- **Workspace.** Save output in a `research/` folder in the current project, creating it if it does not exist. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. If you need the product, the buyer or the decision being studied and the file does not have them, ask once and save the answers there.
- **Finish.** Update `research/README.md`, then reply on one screen as the evidence skill's "How to reply" section describes; its folder is next to this one. Lead with the finding that matters, give at most four more with a quote and a count where the work has them, name the one next step and why, list the files you changed in one line, and end with the "Where you are" line. Detail goes in the file.

## The quote rule

Every finding carries a quote copied character for character from the transcript.

- Never paraphrase inside quotation marks, tidy grammar or merge two remarks.
- Trim with an ellipsis only where words are removed.
- A finding you cannot quote goes in the "Assumptions" section, worded as a question for the next interview.
- Quote the customer only. The interviewer's words are not evidence, and this is the most common mistake: a question the interviewer asked ends up quoted as the customer's view.

## Steps

1. Read the whole transcript before writing anything.
2. Build the timeline in the order events happened, which is rarely the order they were told.
3. Mark the struggling moments: points where the customer was stuck, annoyed, embarrassed or worked around something.
4. Sort what you found into the four forces.
5. Draft candidate job statements.
6. List what is still unknown.

## Output

Write to `research/interviews/<interview-name>.md`. Skip any transcript that already has a summary there unless the user asks to redo it.

```markdown
# <Participant label>: <one-line summary of their story>
Source: <path or link to the transcript>

## Context
Role, company type, what they switched from and to. No names unless the user asked to keep them.

## Timeline
| Stage | What happened | Quote |
| First thought | | |
| Passive looking | | |
| Active looking | | |
| Deciding | | |
| Purchase or staying put | | |
| First use | | |

## Forces
### Push (what was wrong with the old situation)
### Pull (what they hoped the new solution would give them)
### Anxiety (what worried them about the new solution)
### Habit (what kept them attached to the old way)
One bullet per force, each with a quote and the timeline stage it appeared in.

## Candidate jobs
Two or three short statements, solution-free, each with its supporting quote.

## Assumptions and open questions
```

Leave a timeline stage empty and say "not covered" when the interview did not reach it. Do not fill gaps with what probably happened.

## Sorting the forces

- **Push** is about the old situation: "we kept missing renewals".
- **Pull** is about the new one: "I wanted one place to see everything".
- **Anxiety** is a worry about the new solution specifically: cost, migration, whether the team would adopt it.
- **Habit** is attachment to the present: sunk cost, familiarity, "it mostly works".

"The old tool was slow" is a push. It becomes a pull only if they said speed is what drew them to the new one.

## Check before finishing

- Every quote has been checked by script. Follow the evidence skill, whose folder is next to this one: prepare the transcript with `prepare.py`, naming the interviewer, write your findings as evidence records in `research/evidence/interviews.jsonl`, and run `verify_quotes.py` until each one passes or is removed. Without Python, reread the transcript for each quote and mark the summary "Not script-verified".
- The summary describes the customer's situation. If the product is the subject of most sentences, rewrite.
- Events are dated or ordered wherever the customer gave timing.
