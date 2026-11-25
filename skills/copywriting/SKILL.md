---
name: copywriting
description: Write marketing and product copy from Jobs to Be Done research, using the customers' own words and citing the quote behind each line. Covers homepages, landing pages, emails, ads, LinkedIn posts, sales one-pagers, onboarding and in-app copy, and can structure a piece with a named formula such as BAB, PASTOR, QUEST, SLAY, VFCA or the 4 Ps. Use when the user asks for copy, messaging, headlines, a homepage, a landing page, an email, an ad or a post based on what customers said.
---

# Copywriting

Write copy that describes the reader's situation in the words customers used. What you lead with depends on where the reader is in their decision.

## Setup: none required

The user should never have to create folders, rename files or run another skill first.

- **Input.** In order of usefulness: `research/forces.md`, `research/job-statements.md`, `research/job-map.md`, the summaries in `research/interviews/` for quotes, and `research/voc/report.md` for the customers' vocabulary. If there are interview summaries and no forces diagram, build the diagram first by following the forces-of-progress skill. Also read the user's existing copy if they share it or give its address, so you know what the product actually does.
- **Workspace.** Save output in a `research/` folder in the current project, creating it if it does not exist. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. If you need the product, the buyer or the decision being studied and the file does not have them, ask once and save the answers there.
- **Finish.** Reply with a short summary of what you wrote, where it was saved, and the one next step you recommend. Offer to do that step.

## Input

If there is no research, do not write from the product description alone. Tell the user the draft would be generic, and offer two options: plan interviews with the interview-guide skill, or proceed with every line marked as an assumption.

## First, settle two things

Both are choices between known options, and so is the formula in the next section. Ask a choice between known options through your environment's question tool if it has one (`AskUserQuestion` in Claude Code), or as a short numbered list. Ask anything about the user's product or customers in plain text, with no options offered.

1. **The piece.** Homepage, landing page, email, ad, LinkedIn post, sales one-pager, onboarding screen or something else. If the user did not say, ask.
2. **The reader's stage.** Where is the person reading this in the buying timeline? This decides which force leads.

| Reader's stage | They are | Lead with | Typical pieces |
| --- | --- | --- | --- |
| First thought, passive looking | Living with the problem, not yet searching | The strongest push, in their words | Ads, social posts, cold email, top of a homepage |
| Active looking | Comparing options | The strongest pull, and what makes this different | Landing pages, comparison pages, sales one-pagers |
| Deciding | Close, and nervous | The top anxieties, answered | Pricing page, FAQ, trial and demo emails, proposals |
| First use | Signed up, still attached to the old way | The top habits: what carries over and what to do first | Onboarding emails, welcome screens, empty states |
| Drifting away | Using it less | The pushes building inside our own product, and the original pull | Win-back and renewal emails |

A piece aimed at the wrong stage is the most common reason good copy fails. An ad that answers pricing objections is talking to someone who is not there yet.

## Pick a structure

Once you know the piece and the reader's stage, choose how to order it. `references/formulas.md` has six formulas, what each slot holds, and which research fills it:

| Formula | Reach for it when |
| --- | --- |
| BAB (Before, After, Bridge) | The piece is short and the reader is not looking yet |
| SLAY (Story, Lesson, Advice, You) | It is a LinkedIn post and there is a true story to tell |
| The 4 Ps (Picture, Promise, Proof, Push) | It is a landing page or sales email and you have proof |
| QUEST (Qualify, Understand, Educate, Stimulate, Transition) | The page is for one kind of buyer and needs to turn the wrong ones away |
| VFCA (Visceral opener, Fresh perspective, Challenge, Anaphora) | It is an opinion post built on a line a customer said |
| PASTOR (Problem, Amplify, Solution, Testimony, Offer, Response) | It is a long sales page with an offer and publishable testimony |

If the user names a formula, use it. If they do not, pick one, say which and why in a line, and offer the alternative. A homepage usually follows the section map below instead, since it has to answer every force.

The formula sets the order. The research fills the slots. A slot with nothing behind it is marked "NEEDS ANSWER".

## Shapes for common pieces

**Homepage or landing page.** One section per force, in this order:

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

**Email.** One force per email. Subject line from the customer's own phrase for it. Open with their situation, give one idea, and ask for one action. For a sequence, give each email a different force and say which.

**Ad or short social post.** One push or one pull, stated the way a customer said it. BAB fits well. Write five variants on five different forces so they can be tested against each other.

**LinkedIn post.** SLAY when there is a true story, VFCA when there is a strong line and a view. Write in the user's first person, and never invent the story.

**Sales one-pager or deck outline.** Situation (pushes), what they want instead (pulls), why people hesitate and the answer (anxieties), how switching works (habits), proof.

**Onboarding and in-app copy.** Name the step of the job the user is on, using the job map's wording. Tell them what carries over from the old way.

For anything else, apply the stage table and keep the same rules.

## Writing rules

- Use the ranking from the forces diagram. A force mentioned in six of eight interviews earns a place, and one mentioned once does not.
- Use the customers' vocabulary. If they said "chasing invoices", do not write "accounts receivable automation".
- Be specific. Prefer a number, a time or a named situation to an adjective.
- Lead with the reader's situation, and bring the product in second.
- Give options for the line that matters most: five headlines or subject lines, each built on a different force, and say which force each uses.
- Write one answer per anxiety, and say what the product does about it. If you do not know, write "NEEDS ANSWER" for the user to fill in. Never invent a feature, guarantee, price or statistic.
- Customer quotes used as testimonials stay anonymous, with a note that the user needs permission to publish them.

## Output

Write to `research/copywriting/<piece>.md`, for example `homepage.md` or `onboarding-emails.md`:

```markdown
# <Piece>
Reader's stage: <stage>
Structure: <formula or section map, and why>
Based on: <files used>

## Options for the lead line
1. <line>  (push: <force>, 6/8 interviews)

## Draft
The copy, laid out the way the piece will be read.

## Source notes
| Line | Source | Quote |

## Assumptions
Every claim with no research behind it, and every NEEDS ANSWER.
```

## Check before finishing

- The piece leads with the force that matches the reader's stage.
- Every slot of the formula is filled from the research or marked "NEEDS ANSWER". No invented story, testimony or statistic.
- No line promises something the user has not confirmed the product does.
- Every customer quote in the source notes passes the evidence skill's quote check. Its folder is next to this one.
- Read the lead line as the customer. If they would not say it that way, rewrite it.
