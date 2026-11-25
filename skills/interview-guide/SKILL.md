---
name: interview-guide
description: Build a Jobs to Be Done switch-interview guide, with a recruiting screener, a timeline-based discussion guide and a note-taking template. Use when the user is planning customer interviews, asks what to ask customers, or wants an interview script or screener.
---

# Interview Guide

Produce everything a person needs to run switch interviews: who to recruit, how to open, and what to listen for. The interview itself is run by a human. Never simulate a customer or write imagined answers.

## Setup: none required

The user should never have to create folders, rename files or run another skill first.

- **Input.** The user's description of their product and customers, in whatever form they give it. A website, a pitch deck or a product page is enough to start from.
- **Workspace.** Save output in a `research/` folder in the current project, creating it if it does not exist. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Finish.** Reply with a short summary of what you found, where it was saved, and the one next step you recommend. Offer to do that step.

## Before writing

You need three things. Read `research/context.md` first. Ask for whichever are still missing, in one message, then save all three to `research/context.md` so no other skill has to ask again:

1. What the product is, in a sentence.
2. Who makes the buying decision.
3. The decision to understand: why people bought, why they switched away, or why they considered it and stayed put.

The third is a choice between known options. The first two are the user's own words. Ask a choice between known options through your environment's question tool if it has one (`AskUserQuestion` in Claude Code), or as a short numbered list. Ask anything about the user's product or customers in plain text, with no options offered.

## What to produce

Write to `research/interview-guide.md`.

### 1. Screener

Five to seven questions that find people with a recent decision to recall.

- Recruit people who bought, switched or cancelled in the last 90 days. Memory of the sequence fades after that.
- Screen for the person who made the decision, since a user who was handed the tool cannot describe the purchase.
- Include one question that disqualifies people who are only thinking about buying. They describe what they imagine.
- Never reveal which answer qualifies.

### 2. Opening script

Short enough to say aloud in under a minute. It must do three things:

- **Lower the stakes.** "We are early in some research. Some details will matter and some will not. I mostly want to hear the story of how you came to sign up."
- **Distance the interviewer from the product.** They did not design or build it, so nothing said will offend.
- **Set up the documentary.** "Imagine we are filming a documentary about this decision. No detail is too small, including where you were and who else was involved."

Then one opening question: "Tell me about how you came to purchase ___."

### 3. Timeline prompts

The interviewer is filling in this timeline, working backward from the purchase:

| Stage | What to find out |
| --- | --- |
| First thought | When did they first think something had to change? What was happening that day? |
| Passive looking | What did they notice without actively searching? Who did they mention it to? |
| Active looking | What event made them start putting in time? What did they compare? |
| Deciding | What nearly stopped them? What did they give up to choose this? |
| Purchase, or staying put | What happened on the day? Who else had to agree? |
| First use | What did they do first? What did they keep doing the old way? |

For each stage write three or four prompts in plain speech. Prompts ask what happened. Remove any prompt that asks what the customer would want, would pay or would use.

### 4. Interviewer techniques

Include these as a short reminder list:

- Follow the emotional energy. When their voice changes, ask about that moment.
- Play dumb. Ask them to explain terms you already know.
- Once or twice, retell a detail slightly wrong so they correct you and add more.
- Ask "what else was going on then?" before moving to the next stage.

### 5. Note template

A blank forces grid (push, pull, anxiety, habit) and the timeline stages with space for quotes, for the debrief straight after the call.

## Check before finishing

- No leading questions, and none that name a feature.
- No hypothetical questions.
- The guide fits on two pages. An interviewer cannot read more than that during a call.
