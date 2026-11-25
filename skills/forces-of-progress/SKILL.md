---
name: forces-of-progress
description: Synthesize several customer interviews into one Forces of Progress diagram, ranking push, pull, anxiety and habit by how many interviews mention each. Use when the user asks for a forces diagram, why customers switch or churn, or patterns across interviews.
---

# Forces of Progress

Combine interviews into a single view of why customers switch and what holds them back. A customer switches when push plus pull outweighs anxiety plus habit.

## Setup: none required

The user should never have to create folders, rename files or run another skill first.

- **Input.** Start from the interview summaries in `research/interviews/`. If the user points to transcripts that have no summary yet, or there are no summaries at all, analyze those transcripts first by following the interview-analysis skill, then continue. Do this yourself and do not send the user away to run another skill.
- **Workspace.** Save output in a `research/` folder in the current project, creating it if it does not exist. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. If you need the product, the buyer or the decision being studied and the file does not have them, ask once and save the answers there.
- **Finish.** Reply with a short summary of what you found, where it was saved, and the one next step you recommend. Offer to do that step.

## Input

Every force must arrive with a quote and a timeline stage, which is why the summaries come first.

With fewer than three interviews, produce the diagram and state at the top that the ranking is not yet meaningful.

## Steps

1. List every force from every interview, keeping its quote, interview and timeline stage.
2. Group forces that describe the same thing in different words. Name each group in the customers' vocabulary and avoid internal product terms.
3. Count interviews per group. One person raising a point five times counts once.
4. Rank within each of the four forces by that count.
5. Move anything seen in a single interview to "Weak signals".

## Output

Write to `research/forces.md`. If the file exists, update it with the interviews added since, and say how the ranking changed.

```markdown
# Forces of Progress
Based on <n> interviews: <list of files>.

## Summary
Three or four sentences: what starts the search, what draws people in, what nearly stops them.

## Push: what is wrong with the current situation
| Force | Interviews | Typical stage | Strongest quotes |

## Pull: what the new solution promises
## Anxiety: what worries them about switching
## Habit: what keeps them where they are
(same table for each)

## Weak signals
Forces seen once. Worth a question in later interviews.

## What to do with this
- Acquisition: which pulls to make clearer, which anxieties to remove.
- Onboarding: which habits to import, mirror or replace.
- Retention: which pushes are building inside our own product.
```

Show "Interviews" as a fraction such as 6/8. Give up to three quotes per force, from different people.

## Rules

- Counts come from the interviews. Never estimate how common a force is in the market.
- Keep the forces distinct. A worry about migration is an anxiety, while "we have always used spreadsheets" is a habit, even when one customer says both in a breath.
- Recommendations at the end must each point to a force in the tables.
- Carry quotes over unchanged from the summaries.
