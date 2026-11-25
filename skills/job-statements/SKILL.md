---
name: job-statements
description: Write and review Jobs to Be Done job statements (functional, emotional and social) from customer research. Use when the user asks for JTBD statements, the core job of their customer, or wants existing job statements critiqued.
---

# Job Statements

Draft the jobs customers are hiring a product to do, then test each statement against the rules below. Review is half the work: a list of plausible statements that nobody has checked is worse than three good ones.

## What a job is

A Job to Be Done:

1. **Is solution-agnostic.** It does not know which products exist.
2. **Results in progress when completed.** The customer is better off.
3. **Is relatively stable across time.** People had this job decades ago and will have it decades from now.

| Poorly worded | Well worded |
| --- | --- |
| Get my floor as clean as possible when I vacuum. | Maintain a clean living space. |
| Edit my photos and provide a variety of professional filters. | Share beautiful pictures. |
| Help me maximize my deductions and get as much back as possible. | File my taxes with confidence. |
| Let me add tags, labels and folders to my email. | Find emails and files quickly. |

The left column is tied to a product, so it can only lead to a better version of that product.

## Input

Interview summaries, the forces diagram, support tickets or sales notes. If the user has no research, say that the statements will be hypotheses, draft them, and label every one "untested".

## Steps

1. Collect what customers said they were trying to get done, in their words.
2. For each, ask "why?" until the answer stops mentioning a tool. Stop before it becomes a life goal such as "be successful".
3. Write the statement: a verb, an object, and a context only if it changes the meaning. Keep it short.
4. Sort into three kinds:
   - **Functional**: the task. "Send invoices that get paid on time."
   - **Emotional**: how they want to feel. "Feel confident nothing has slipped through."
   - **Social**: how they want to be seen. "Look organized to a new client."
5. Review every statement and mark it pass or fail on each check.

## Review checks

- Starts with a verb.
- Names no product, feature, technology or channel.
- Holds one job. Split statements joined by "and".
- Would have been true ten years ago.
- Could be done with at least two different kinds of solution.
- Is supported by a quote.

Rewrite statements that fail, and show the original beside the rewrite so the user can see what changed.

## Output

Write to `research/analysis/job-statements.md`:

```markdown
# Job statements

## Core job
The one functional job the others support, with the evidence for choosing it.

## Functional jobs
| Statement | Interviews | Quote | Checks |

## Emotional jobs
## Social jobs

## Rejected or rewritten
| Original | Problem | Rewrite |
```

Put the best-evidenced jobs first. If no job has support from more than one interview, say so above the tables.
