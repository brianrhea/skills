---
name: ask-brian
description: Ask which skill fits your situation and what to do next. Starts from where you are (an idea, a business with customer data, or a new market) and does the next step.
disable-model-invocation: true
---

# Ask Brian

You do not need to remember every skill or the order they go in, so ask. This skill finds out where the user is starting from, tells them where they stand, and does the next useful thing.

Before describing what another skill does in detail, read its SKILL.md: the tables below are for orientation.

## Setup: none required

- **Workspace.** Everything these skills produce lives in a `research/` folder in the current project. Create it when something first needs saving. Never ask the user to create folders or move files.
- **Context.** `research/context.md` holds the starting point, the product, the buyer and the decision being studied. Every other skill reads this file, so the user is asked once.

## Steps

1. **Look before asking.** Read `research/` if it exists, and whatever the user gave you in this message: files, pasted text, links.
2. **Find the starting point.** If the files or the message make it obvious, do not ask. Otherwise ask the question under "Where are you starting from?".
3. **Say where they stand** in two or three lines: what exists, what is missing, and the next step you recommend with the reason.
4. **Do the step** by following the matching skill.
5. **Close** with what was saved and what comes next.

## How to ask

There are two kinds of question, and they are asked differently.

**A choice between known options** goes through your environment's question tool if it has one. In Claude Code that is `AskUserQuestion`; other agents have their own, and some have none. Without one, ask in plain text with a short numbered list.

- Two to four options, each a few words, with a one-line description.
- Put the option you would pick first when you have a recommendation.
- The user can always answer in their own words. Never make them choose a wrong option.
- Use multiple-select when more than one can be true, such as what material they have.

**Anything about the user's idea, their customers or what happened** is asked in plain text and answered in their own words. Never offer options for these. A menu of likely answers puts words in their mouth, which is the mistake this whole method exists to avoid.

Keep it short. Ask at most three questions before doing something useful. Never ask what a file already answers. Save every answer to `research/context.md`.

## Where are you starting from?

Ask this once, as a choice:

| Option | Description to show |
| --- | --- |
| I have an idea | No customers yet, or only a handful. I want to know if the problem is real. |
| I have customers and data | Calls, tickets or survey comments are piling up. I have never dug into them this way. |
| I'm looking at a new market | An adjacent market or a new segment for a product that already exists. |
| I'm partway through | Pick up where the research left off. Offer this only when `research/` has work in it. |

Then, where it helps, one or both of these as choices:

- **What do you have on hand?** (multiple-select) Interview transcripts. Sales or support calls. Tickets or survey comments. Nothing yet.
- **What is this for?** Deciding what to build. Positioning and messaging. Deciding whether to enter a market. Understanding why customers leave.

And these in plain text, in their words: what the product or idea is, who it is for, and what made them want to look into this now.

## Starting from an idea

The goal is to find out whether the problem is real before anything gets built. Everything produced here is a hypothesis, to be proven wrong as cheaply as possible.

1. **Hear the idea.** Ask them to describe it, who has the problem, and what those people do about it today. Plain text.
2. **Turn it around.** Restate it as the customer's problem with the product taken out. If it cannot be stated without the product, say so; that is the first finding.
3. **Draft the hypotheses**, each marked "untested", and save them to `research/hypotheses.md`:
   - The job the customer is trying to get done, following job-statements.
   - What they use today, including spreadsheets, workarounds and doing nothing, following Part 1 of competitive-analysis.
   - A first guess at the four forces: what would push them, what would pull them, what would worry them, what habit they would have to break.
   - The five things worth learning from each conversation: the progress they want, the context they are in, the obstacles, the hacks they use today, and how they judge quality.
4. **Name the riskiest guess.** Usually it is whether the problem hurts enough for anyone to change what they do.
5. **Plan five conversations** with interview-guide. People who have the problem today, asked about what they have already tried and paid for, never whether they would use this.
6. **After the conversations,** use interview-analysis, then come back and mark each hypothesis supported, wrong or still open.

Say this plainly at least once: an agent can produce a convincing job map for an idea in a minute, and it will be made of the agent's assumptions. It is worth having as a list of things to check.

## Starting from customers and data

The business works and the material exists. Nobody has read it with this lens.

1. **Read what they have.** voice-of-customer on the calls, tickets and survey comments. This gives themes, the customers' vocabulary and a list of people worth talking to.
2. **See what they are compared with.** competitive-analysis, starting from the alternatives customers named.
3. **Talk to recent buyers.** interview-guide for switch interviews with five to eight people who bought or cancelled in the last 90 days. The pile of feedback says what people complain about. Only these conversations say why they bought.
4. **Find the pattern.** interview-analysis for each, then forces-of-progress and job-statements.
5. **Decide what matters.** job-map, then outcome-survey to rank the unmet needs across the customer base.
6. **Put it to work.** copywriting.

Most people stop after step 1 because the themes feel like answers. Tell them the themes are good hunches and recommend step 3.

## Starting from a new market

The product exists. The question is whether a different group of people would hire it, and for what.

1. **Pin down the job current customers hire it for.** Take it from `research/job-statements.md` or the forces diagram. If neither exists, ask what their best customers were trying to get done, and mark the answer as their belief.
2. **Ask which kind of move this is,** as a choice: the same job for a different kind of customer, or a neighbouring job for the customers they already have.
3. **Keep the new work apart.** Save everything for the new market under `research/markets/<name>/` so it never mixes with evidence from current customers.
4. **Find out what that market uses today.** competitive-analysis for the new segment. Expect different alternatives from the ones current customers named.
5. **Plan five conversations** with interview-guide, with people in the new market who have the problem today and are not customers.
6. **Compare.** After interview-analysis, set the new market's forces beside the current one's. Different pushes and the same pull is promising. A different job altogether means a different product.

Warn them about the common mistake: assuming the new market wants the product for the reason current customers do.

## Partway through

| The user has | Next step | Skill |
| --- | --- | --- |
| Only an idea of who to talk to | Plan the interviews | interview-guide |
| A few interview transcripts without summaries | Summarize each one | interview-analysis |
| A large pile of feedback: tickets, sales calls, survey comments, cancellations, deal notes | Find the themes, with checked quotes and counts | voice-of-customer |
| A question about competitors or what customers use instead | Map the alternatives and profile competitors | competitive-analysis |
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
Starting point: <an idea | customers and data | a new market: name>

| Step | Status | File |
| --- | --- | --- |
| Hypotheses | 6 drafted, 2 supported, 1 wrong | hypotheses.md |
| Interview guide | done | interview-guide.md |
| Feedback themes | 412 tickets, 3 months old | voc/report.md |
| Competitors | 4 profiled | competitors/ |
| Interviews analyzed | 5 of 8 | interviews/ |
| Forces of Progress | from 5 interviews, out of date | forces.md |
| Job statements | not started | |
| Job map | not started | |
| Outcome survey | not started | |
| Copywriting | not started | copywriting/ |

Next: analyze the three new transcripts, then refresh the forces diagram.
```

Leave out rows that do not apply to the starting point. Mark a file "out of date" when something it depends on has changed since it was written, such as new interviews after the forces diagram.

## Rules

- When the user has no research and wants output anyway, say plainly that the result will be a hypothesis. Then help them. The fastest honest route is usually an interview guide and five conversations.
- Never invent customers, interviews or quotes to fill a gap in the path.
- Findings from tickets, reviews and public pages are hypotheses. When the next step is a decision that rests on them, recommend confirming with a few interviews first.
- Recommend one next step at a time.
