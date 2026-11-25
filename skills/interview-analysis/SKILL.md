---
name: interview-analysis
description: Analyze a customer interview transcript with Jobs to Be Done, extracting the buying timeline, struggling moments and Forces of Progress with verbatim quotes. Use when the user shares or points to interview transcripts, call recordings as text, or asks what a customer said.
---

# Interview Analysis

Turn one transcript into a one-page summary that a person who was not on the call can trust. Handle one interview at a time. When given a folder, repeat the process for each file and write one summary per interview.

## The quote rule

Every finding carries a quote copied character for character from the transcript.

- Never paraphrase inside quotation marks, tidy grammar or merge two remarks.
- Trim with an ellipsis only where words are removed.
- A finding you cannot quote goes in the "Assumptions" section, worded as a question for the next interview.
- Quote the customer only. The interviewer's words are not evidence.

## Steps

1. Read the whole transcript before writing anything.
2. Build the timeline in the order events happened, which is rarely the order they were told.
3. Mark the struggling moments: points where the customer was stuck, annoyed, embarrassed or worked around something.
4. Sort what you found into the four forces.
5. Draft candidate job statements.
6. List what is still unknown.

## Output

Write to `research/analysis/<interview-name>.md`:

```markdown
# <Participant label>: <one-line summary of their story>

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

- Search the transcript for three of your quotes and confirm they match exactly.
- The summary describes the customer's situation. If the product is the subject of most sentences, rewrite.
- Events are dated or ordered wherever the customer gave timing.
