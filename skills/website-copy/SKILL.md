---
name: website-copy
description: Write homepage or landing page copy from Jobs to Be Done research, mapping the core job and the Forces of Progress to page sections and citing the customer quote behind each line. Use when the user asks for website copy, a homepage, a landing page, headlines or messaging based on customer research.
---

# Website Copy

Write a page that describes the visitor's situation in the words customers used. Each section answers one of the forces that decide whether they switch.

## Input

In order of usefulness: the forces diagram (`research/analysis/forces.md`), job statements, the job map, and interview summaries for quotes.

If there is no research, do not write the page from the product description alone. Tell the user the draft would be generic, and offer two options: run the interview-guide skill first, or proceed with every line marked as an assumption.

## Map research to the page

| Section | Source | Job on the page |
| --- | --- | --- |
| Headline | Core job | Say what the visitor is trying to get done |
| Subhead | Strongest pull | Say what life looks like once it is done |
| Problem | Top two or three pushes | Show the moment they started looking |
| How it works | Job map steps | Follow their job in order |
| Objections | Top anxieties | Answer what nearly stopped buyers |
| Switching | Top habits | Explain import, setup and what stays the same |
| Proof | Quotes | Let a peer say it |
| Call to action | First step of the job | Ask for a small next step |

Use the ranking from the forces diagram. A force mentioned in six of eight interviews earns a section, and one mentioned once does not.

## Writing rules

- Use the customers' vocabulary. If they said "chasing invoices", do not write "accounts receivable automation".
- Be specific. Prefer a number, a time or a named situation to an adjective.
- Lead each section with the customer's situation, and bring the product in second.
- Give five headline options, each built on a different push or pull, and say which force each uses.
- Give three options for the call to action.
- Write one answer per anxiety, and say what the product does about it. If you do not know, write "NEEDS ANSWER" for the user to fill in. Never invent a feature, guarantee, price or statistic.
- Customer quotes used as testimonials stay anonymous, with a note that the user needs permission to publish them.

## Output

Write to `research/copy/homepage.md`:

```markdown
# Homepage draft
Based on: <files used>

## Headline options
1. <headline>  (push: <force>, 6/8 interviews)

## Subhead
## Problem
## How it works
## Objections
## Switching
## Proof
## Call to action

## Source notes
| Line | Source | Quote |

## Assumptions
Every claim with no research behind it, and every NEEDS ANSWER.
```

## Check before finishing

- Each top anxiety is answered somewhere on the page.
- No line promises something the user has not confirmed the product does.
- Read the headline as the customer. If they would not say it that way, rewrite it.
