---
name: job-canvas
description: Explore the Jobs to Be Done behind an idea, a product or a role before any research exists. Proposes candidate job statements, helps the user pick one at the right level, and builds a hypothesis canvas with the performer, related jobs, emotional and social aspects, a job map, forces and a buying timeline, each marked untested. Use when the user has an idea or a product and wants to think through the job, asks what job a product is hired for, or wants a JTBD canvas.
---

# Job Canvas

Turn an idea into a set of things worth checking. In a few minutes the user goes from "I want to build X" to a chosen job, a picture of who does it, and a list of assumptions to test in conversations.

Everything this skill produces is a hypothesis. It comes from what you already know about the world, which is the same thing every competitor's agent knows. It earns its keep by telling the user exactly what to go and find out.

## Setup: none required

- **Workspace.** Save output to `research/job-canvas.md`, creating `research/` if needed. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. Save the starting point, the product or idea and the performer there when the user gives them.
- **Finish.** Reply with the chosen job, the three riskiest assumptions, where the canvas was saved, and the next step. Offer to write the interview guide.

## How to ask

A choice between known options goes through your environment's question tool if it has one (`AskUserQuestion` in Claude Code), or a short numbered list. Two to four options, your recommendation first, and the user can always answer in their own words.

The idea itself, and anything about real customers, is asked in plain text. Never offer options for those.

## Steps

### 1. What are we exploring?

Ask as a choice:

| Option | What it means |
| --- | --- |
| A product or service | Start from the thing: "meal kits", "expense software" |
| A role | Start from the person: "office manager", "new parent" |
| I already know the job | Skip to step 4 with their statement |

Then ask, in plain text, what it is. One line is enough.

### 2. Which way of writing jobs do they prefer?

Ask as a choice:

| Option | Looks like |
| --- | --- |
| Verb + object + clarifier | "Facilitate a workshop online" |
| When I, help me, so I can | "When I chop an onion, help me slice it evenly, so I can get dinner on the table" |

Recommend the first. It is shorter and easier to compare. Use the chosen style for the rest of the session.

### 3. Propose five candidate jobs

Write five jobs that people hire this product for, or that this role is trying to get done. Each one:

- Reflects the person's point of view, not the company's.
- Starts with a verb.
- Names no product, feature or technology.
- Would still be true in ten years.

Show the four strongest as a choice and say that they can write their own. Let them edit the wording.

### 4. Check the level

Jobs come at different sizes, and most first attempts are too big or too small. Write the chosen job at four levels:

| Level | What it is | Example |
| --- | --- | --- |
| Aspiration | What they want their life or work to be | Be a parent who is present |
| Big job | The main thing they are trying to get done | Feed my family well on weeknights |
| Little job | A part of the big job | Plan the week's dinners |
| Micro job | A single task | Find a recipe for what is in the fridge |

Ask which level to work at, as a choice. Recommend the big job or a little job: an aspiration is too broad to build for, and a micro job is a feature.

### 5. Who does the job?

Propose three kinds of people who do this job, described by their situation and not only a title. Ask which to focus on, as a choice. The person who does the job is not always the person who pays; note both when they differ.

### 6. Build the canvas

For the chosen job and performer, draft each section. Three items each unless noted.

| Section | How to write it |
| --- | --- |
| Aspiration | One line starting "So I can…" |
| Related jobs | Three each: must-have, nice-to-have and aspirational jobs the same person has nearby |
| Emotional aspects | Start with "Feel…" or "Avoid feeling…" |
| Social aspects | Start with "Appear as…" or "Avoid appearing as…" |
| Differentiators | Circumstances that change how the job gets done, written "If … vs. …" |
| Job map | The eight stages, two to six steps each, following the job-map skill |
| Outcomes | For the two stages that look hardest: "Minimize the time it takes to…" or "Minimize the likelihood of…" |
| What they use today | Products, workarounds and doing nothing, following Part 1 of competitive-analysis |
| Forces | Three each: push, pull, anxiety and habit |
| Buying timeline | What probably happens at first thought, passive looking, active looking, deciding, first use and ongoing use |

Job steps use plain verbs with no adjectives: "Gather the figures", never "Quickly gather accurate figures".

### 7. Name the riskiest assumptions

Pick the three items the idea depends on most. Usually: that the push is strong enough to make anyone change, that the performer you chose is the one who feels it, and that what they use today is as bad as you think. Turn each into something to listen for in a conversation.

## Output

Write to `research/job-canvas.md`:

```markdown
# Job canvas: <job>
Status: hypothesis. Nothing here has been checked with a customer.
Exploring: <product, service or role> · Level: <level> · Performer: <performer>

## The job
<statement, in the chosen style>
Aspiration: So I can <…>

## Riskiest assumptions
1. <assumption> → listen for: <what would confirm or kill it>

## Canvas
| Section | Item | Status | Evidence |
| --- | --- | --- | --- |
| Emotional | Feel in control of the week | untested | |

## Job map
## What they use today
## Forces
## Buying timeline
```

`Status` is one of `untested`, `supported` or `wrong`.

## After interviews

When interview summaries exist in `research/interviews/`, go back through the canvas:

- An item a customer confirmed becomes `supported`, with the quote and participant code in `Evidence`. Check new quotes with the evidence skill's script; its folder is next to this one.
- An item a customer contradicted becomes `wrong`. Keep it in the file. Knowing what turned out false is worth as much as what turned out true.
- Add what customers said that the canvas never guessed. These are the most valuable rows.
- Report how many items moved, and update the status line at the top once most of the canvas rests on evidence.

## Rules

- Never present the canvas as research. Say "hypothesis" at the top of the file and in your reply.
- Do not build a survey or write copy from an untested canvas without telling the user what it rests on.
- Do not invent a customer, a quote or a statistic to make an item look supported.
- Three good items beat ten plausible ones. Leave a section short when you have little to go on.

The canvas sections follow Jim Kalbach's JTBD Canvas. The related-jobs spectrum is Bob Moesta's, the job map is Tony Ulwick and Lance Bettencourt's, and the forces and timeline come from Bob Moesta and Chris Spiek.
