---
name: job-map
description: Create a Jobs to Be Done job map that breaks a core job into the eight universal steps (define, locate, prepare, confirm, execute, monitor, modify, conclude) with outcome statements for each. Use when the user asks for a job map, the steps of a customer's job, or outcome statements.
---

# Job Map

Describe what the customer is trying to get done from start to finish, without reference to any product. The map shows every point where a product could help.

## Input

A core job statement. If the user gives a product or a feature, work out the job with them first, or use the job-statements skill. Research is optional and makes the map far more useful.

## The eight steps

| Step | The customer is | Ask |
| --- | --- | --- |
| 1. Define | Deciding goals and planning the approach | What must they work out before starting? |
| 2. Locate | Gathering inputs | What information or materials must they find? |
| 3. Prepare | Setting up | What has to be organized or cleaned first? |
| 4. Confirm | Checking readiness | What do they verify before committing? |
| 5. Execute | Doing the core task | What is the central activity? |
| 6. Monitor | Checking progress | How do they know it is working? |
| 7. Modify | Adjusting | What do they change when it is off course? |
| 8. Conclude | Finishing | What wraps the job up or prepares for next time? |

## Writing the steps

- Each step is a verb and an object, describing a goal: "Gather last quarter's figures".
- Name no tool, including spreadsheets, email and the user's own product. "Open the dashboard" is an action inside a solution.
- A step may hold two or three sub-steps when customers treat them as separate efforts.
- Keep the order customers follow, even where it loops.
- All eight appear. If one seems empty, write what customers do without noticing and mark it for an interview question.

## Outcome statements

For each step, write three to eight outcomes customers use to judge success. Use this form:

**Minimize** + **the time it takes to / the likelihood of / the amount of** + **object** + **context**

- "Minimize the time it takes to reconcile figures from different sources."
- "Minimize the likelihood of presenting a number that is later corrected."

Each outcome is measurable, holds one idea and names no solution.

## Grounding

When research exists, mark every step and outcome:

- **Supported**: with the quote and interview.
- **Assumed**: nothing in the research confirms it.

Without research, mark the whole map "hypothesis" in its first line.

## Output

Write to `research/analysis/job-map.md`:

```markdown
# Job map: <core job>
Status: grounded in <n> interviews | hypothesis

## Overview
| Step | What the customer does | Evidence |

## 1. Define
What the customer does, then the outcome statements, each marked supported or assumed.
(repeat for all eight)

## Where customers struggle most
The two or three steps with the most pushes and workarounds in the research.

## Questions for the next interviews
One per assumed step.
```

The numbered outcome statements are the input to the outcome-survey skill, so keep the wording final and the numbering stable.
