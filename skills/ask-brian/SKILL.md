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
3. **When `research/` has work in it, greet in two lines.** First line: what the project is and what happened last, from `research/README.md`. Second line: the "Where you are" line. If files have arrived since the README was written, say so. Then, if the next step is work you can do alone, do it now. If it needs the user ("talk to four more customers"), ask in plain text whether it happened and where the notes are.
4. **Do the step** by following the matching skill. When the message already says what they want ("forces from these five calls"), skip the questions and do it.
5. **Close** the way the evidence skill's "How to reply" section describes.

## How to ask

There are two kinds of question, and they are asked differently.

**A choice between known options** goes through your environment's question tool if it has one. In Claude Code that is `AskUserQuestion`; other agents have their own, and some have none. Without one, ask in plain text with a short numbered list.

- Two to four options, each a few words, with a one-line description.
- Put the option you would pick first when you have a recommendation.
- The user can always answer in their own words. Never make them choose a wrong option.
- The short label above each question is twelve characters or fewer: "Start", "Goal", "Job", "Next".

**Anything about the user's idea, their customers or what happened** is asked in plain text and answered in their own words. Never offer options for these. A menu of likely answers puts words in their mouth, which is the mistake this whole method exists to avoid.

Ask one thing at a time, and only what changes which step runs next. Never ask what a file or the message already answers. Save every answer to `research/context.md`.

Read the person without asking them. Someone who says "forces", "switch interview" or "job map" gets short replies and no definitions. Someone who says "I have an idea for an app" gets each term explained once, in a clause, the first time it appears.

## Where are you starting from?

With nothing in the message or the folder, ask this once, as a choice:

| Option | Description to show |
| --- | --- |
| An idea | No customers yet, or only a handful. I want to know if the problem is real. |
| Customers and data | Calls, tickets or survey comments are piling up. Nobody has dug into them this way. |
| A new market | An adjacent market or a new segment for a product that already exists. |

Then ask the one plain-text question for that starting point, and nothing else until you have done something useful:

| Starting point | The one question |
| --- | --- |
| An idea | Tell me the idea in a sentence or two, and who has the problem. |
| Customers and data | Where's the material? Point me at a folder or files, or paste it. |
| A new market | Which market, and what made you look at it now? |

**When there is customer material and no stated purpose,** ask one more thing before reading it, as a choice: *What will you do with what we find?*

| Option | Where it leads |
| --- | --- |
| Rewrite our messaging | Interviews or themes, then forces, then copywriting |
| Decide what to build | Forces, job statements, job map, then the survey |
| Find out why people leave | Cancellations and churn interviews first |
| See what's in there | Themes, then recommend from what turns up |

The answer decides the path, so it comes before the work, not after.

Infer the product, the buyer and the decision from the material. Say what you inferred in one line, save it to `research/context.md`, and let them correct it.

## Starting from an idea

The goal is to find out whether the problem is real before anything gets built. Everything produced here is a hypothesis, to be proven wrong as cheaply as possible.

1. **Hear the idea.** Ask them to describe it, who has the problem, and what those people do about it today. Plain text.
2. **Turn it around.** Restate it as the customer's problem with the product taken out. If it cannot be stated without the product, say so; that is the first finding.
3. **Build the canvas** by following job-canvas. It proposes candidate jobs for the user to choose from, checks the job is at a useful level, picks who does it, and drafts the canvas, job map, forces and buying timeline, every item marked "untested". The user makes those choices. Do not make them on their behalf to save time.
4. **Name the riskiest assumptions.** job-canvas ends with three. Usually the first is whether the problem hurts enough for anyone to change what they do.
5. **Plan five conversations** with interview-guide, as job interviews. People who do the job today, asked about what they have already tried and paid for, never whether they would use this.
6. **After the conversations,** use interview-analysis, then go back to job-canvas to mark each item supported or wrong and add what nobody guessed.

## Starting from customers and data

The business works and the material exists. Nobody has read it with this lens.

1. **Read what they have, by what it is.** Interviews about a decision to buy, switch or cancel, even two or three, go to interview-analysis, one summary each. Piles of tickets, survey comments, sales calls or cancellations go to voice-of-customer, which gives themes, the customers' vocabulary and a list of people worth talking to. With both, do the interviews first and use the pile to check whether what they say holds up across more customers.
2. **See what they are compared with.** competitive-analysis, starting from the alternatives customers named.
3. **Talk to recent buyers.** interview-guide for switch interviews with five to eight people who bought or cancelled in the last 90 days. The pile of feedback says what people complain about. Only these conversations say why they bought.
4. **Find the pattern.** interview-analysis for each, then forces-of-progress and job-statements.
5. **Decide what matters.** job-map, then outcome-survey to rank the unmet needs across the customer base.
6. **Put it to work.** copywriting.

Most people stop after step 1 because the themes feel like answers. Tell them the themes are good hunches and recommend step 3.

## Starting from a new market

The product exists. The question is whether a different group of people would hire it, and for what.

1. **Pin down the job current customers hire it for.** Take it from `research/job-statements.md` or the forces diagram. If neither exists, ask what their best customers were trying to get done, and mark the answer as their belief.
2. **Ask which kind of move this is,** as a choice: "Same job, new customers" or "New job, same customers".
3. **Keep the new work apart.** Save everything for the new market under `research/markets/<name>/` so it never mixes with evidence from current customers.
4. **Find out what that market uses today.** competitive-analysis for the new segment. Expect different alternatives from the ones current customers named.
5. **Plan five conversations** with interview-guide, with people in the new market who have the problem today and are not customers.
6. **Compare.** After interview-analysis, set the new market's forces beside the current one's. Different pushes and the same pull is promising. A different job altogether means a different product.

Warn them about the common mistake: assuming the new market wants the product for the reason current customers do.

## Partway through

| The user has | Next step | Skill |
| --- | --- | --- |
| An idea, a product or a role, and no research | Explore the job and list what to test | job-canvas |
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

`research/README.md` records where the project stands. Its format, the "Where you are" line and the shape of every reply are in the evidence skill, whose folder is next to this one. Read it before your first reply.

## Rules

- When the user has no research and wants output anyway, say plainly that the result will be a hypothesis. Then help them. The fastest honest route is usually an interview guide and five conversations.
- Never invent customers, interviews or quotes to fill a gap in the path.
- Findings from tickets, reviews and public pages are hypotheses. When the next step is a decision that rests on them, recommend confirming with a few interviews first.
- Recommend one next step at a time, and do one step per reply unless the user asked for several.
