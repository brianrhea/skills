---
name: ask-brian
description: Ask which skill fits your situation and what to do next. Looks at your research so far and does the next step.
disable-model-invocation: true
---

# Ask Brian

You do not need to remember every skill or the order they go in, so ask. This skill looks at what the user has, tells them where they are, and does the next useful thing.

Jobs to Be Done research is the path these skills cover today. Before describing what another skill does in detail, read its SKILL.md: the table below is for orientation.

## Setup: none required

- **Workspace.** Everything these skills produce lives in a `research/` folder in the current project. The folder is shared: interviews and context saved here serve any research method, and Jobs to Be Done is the first. Create it when something first needs saving. Never ask the user to create folders or move files.
- **Context.** `research/context.md` holds the product, the buyer and the decision being studied. If it is missing, ask for those three things in one message and save them. Every other skill reads this file, so the user is asked once.

## Steps

1. **Look before asking.** Read `research/` if it exists. Then look at what the user gave you in this message: files, pasted text, links.
2. **Work out where they are** using the table below.
3. **Say it in two or three lines:** what exists, what is missing, and the next step you recommend with the reason.
4. **Do the step** by following the matching skill. If the user's message already makes the step obvious, such as a pasted transcript, skip the question and start.
5. **Close** with what was saved and what comes next.

## The path

| The user has | Next step | Skill |
| --- | --- | --- |
| Nothing yet, or only an idea of who to talk to | Plan the interviews | interview-guide |
| Transcripts without summaries | Summarize each one | interview-analysis |
| Three or more summaries | Find the pattern across them | forces-of-progress |
| A forces diagram | Name the jobs | job-statements |
| A core job | Map its steps and outcomes | job-map |
| A job map, and a need to prioritize | Survey customers | outcome-survey |
| Survey responses | Score them | outcome-survey |
| Forces and job statements, and something to write | Draft the copy | copywriting |

The path is a default. A user who only wants homepage copy from last quarter's interviews does not need a survey. Go straight to what they asked for and fill in only the steps it depends on.

## Status file

Keep `research/README.md` current after every step, so the user and any later session can see the state of the project at a glance:

```markdown
# Research: <product>

| Step | Status | File |
| --- | --- | --- |
| Interview guide | done | interview-guide.md |
| Interviews analyzed | 5 of 8 | interviews/ |
| Forces of Progress | from 5 interviews, out of date | forces.md |
| Job statements | not started | |
| Job map | not started | |
| Outcome survey | not started | |
| Copywriting | not started | copywriting/ |

Next: analyze the three new transcripts, then refresh the forces diagram.
```

Mark a file "out of date" when something it depends on has changed since it was written, such as new interviews after the forces diagram.

## Rules

- When the user has no research and wants output anyway, say plainly that the result will be a hypothesis. Then help them. The fastest honest route is usually an interview guide and five conversations.
- Never invent customers, interviews or quotes to fill a gap in the path.
- Recommend one next step at a time.
