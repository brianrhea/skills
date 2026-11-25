---
name: competitive-analysis
description: Map the real alternatives customers use, including spreadsheets, workarounds and doing nothing, then research named competitors from their public websites, pricing pages, changelogs and docs, with a source and date for every claim. Use when the user asks for a competitive analysis, a competitor comparison, a pricing teardown, what competitors are doing, or who they are really competing with.
---

# Competitive Analysis

Your competitors are whatever customers would use if your product did not exist. That is often a spreadsheet, an intern, three tools taped together, or nothing at all. This skill starts there, from what customers say they hire instead, and only then looks at the companies in your category.

It produces two things: a map of the alternatives, built from your research, and a profile of each named competitor, built from what they publish.

## Setup: none required

- **Input.** Your research so far, and the names or addresses of competitors if you have them.
- **Workspace.** Save output in `research/competitors/`, creating it if needed. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. If you need the product, the buyer or the decision being studied and it is not there, ask once and save the answers.
- **Finish.** Reply with what customers really compare you with, the two or three findings that matter, where the files are, and the one next step you recommend.

## Part 1: What customers hire instead

1. Look in `research/` for what customers have named: tools, workarounds and old habits in interview summaries, the forces diagram and `research/voc/`. Collect each with its quote.
2. If there is no research, ask the user two questions: what were your last few customers using before, and what do people who do not buy end up doing? Mark every answer as the user's belief, to be checked in interviews.
3. Include the alternatives that are not products: doing it by hand, a spreadsheet, hiring someone, putting up with it.
4. Write `research/competitors/alternatives.md`:

```markdown
# What customers hire instead
| Alternative | Kind | Why they use it | Where it falls short | Evidence |
```

`Kind` is one of: direct competitor, different kind of product, workaround, doing nothing. `Evidence` is a verified quote with its participant code, or "user's belief".

The rows with the most evidence are your real competition, whatever category they belong to.

## Part 2: What named competitors publish

Profile three to five competitors: the ones customers named, then any the user adds.

For each, read what the company itself publishes, in this order: home page, pricing, product or features pages, changelog or release notes, documentation, customer stories, careers page. `references/public-sources.md` says what each page tells you and what you may and may not read.

1. **Save what you read.** Put the text of each page in `research/competitors/snapshots/<name>/<date>-<page>.md` with its address at the top. This is your record of what the page said on that day.
2. **Record claims with their source.** Every fact in a profile carries the page address and the date you read it.
3. **Keep three voices apart:** what the company claims, what a customer said, and what you infer. Label each.
4. **Write "not stated publicly"** when a page does not say. Do not guess a price, a customer count or a feature.
5. **Pricing** follows `references/pricing-teardown.md`.

Write one file per competitor, `research/competitors/<name>.md`:

```markdown
# <Competitor>
Read on <date>. Sources listed at the end.

## Who they say it is for
## The promise in their headline
## How they describe the problem
## Pricing
What is charged for, the tiers, what triggers an upgrade, what is hidden behind "contact sales".
## What they have shipped lately
From the changelog, with dates. What the pattern suggests they are betting on.
## What they do more of than customers seem to need
## What their customers say
Only from material the user supplied or your own research. Otherwise: "No customer evidence gathered."
## Not reachable
Pages that were blocked or needed a login.
## Sources
| Claim | Address | Read on | Voice |
```

## Part 3: Comparison

Write `research/competitors/comparison.md`:

- A table with one row per alternative from Part 1, including the workarounds and doing nothing, and columns for who it suits, what it costs in money and effort, what it does well and where it falls short.
- **Where they over-serve.** Things competitors keep adding that your evidence suggests customers do not value. These are places to do less on purpose.
- **Where everyone under-serves.** Problems in your research that no alternative handles well.
- **What to check next.** The claims that rest on belief, and who to ask.

Every cell carries a source or says "not stated publicly". Do not produce a list of strengths, weaknesses, opportunities and threats; it reads well and decides nothing.

## Running it again

When snapshots already exist, read the same pages again, save new snapshots, and compare them with the last ones. Write `research/competitors/changes.md` with what changed and when: price, tiers, headline, who it is for, notable releases. List only real changes, most important first.

## Rules for public sources

- Read a company's own pages freely. They published them to be read.
- If a page refuses you, asks you to sign in or shows a challenge, record it under "Not reachable" and move on. Do not try another route to the same content.
- Do not collect reviews, forum posts or social media in bulk. Review sites and communities forbid it. If the user wants customer opinion about a competitor, ask them to paste or export what they have, then treat it as in voice-of-customer.
- Fetch the page itself for anything about price, terms or dates. Search results are often out of date.
- Quote a sentence or two at most from any page, with its address.
- An archived copy of a page shows what it said on an earlier date. Use it for how pricing and positioning have moved, and give the archive date.
