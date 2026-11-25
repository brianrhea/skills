---
name: voice-of-customer
description: Analyze a large body of existing customer feedback, such as support tickets, sales and success call transcripts, survey comments, cancellation reasons, deal notes or reviews of the user's own product, into themes with counts and verified quotes. Use when the user has many transcripts or an export from a support, CRM, survey or call-recording tool, asks what customers are saying, or wants win/loss, churn or feedback analysis.
---

# Voice of Customer

Turn a pile of what customers already said into themes you can trust, and into a short list of people worth talking to. This is for volume: dozens of calls, hundreds of tickets, thousands of survey comments. For one switch interview read closely, use interview-analysis.

What comes out is a set of well-evidenced hypotheses. Existing feedback tells you what people complain about and ask for. It does not tell you why they bought, and it cannot rank needs across your whole market.

## Setup: none required

- **Input.** Take the data from wherever it is. See "Getting the data" below.
- **Workspace.** Save output in `research/voc/`, creating it if needed. If you cannot write files, give the full output in your reply and say that it was not saved.
- **Context.** Read `research/context.md` if it exists. If you need the product, the buyer or the decision being studied and it is not there, ask once and save the answers.
- **Finish.** Reply with the three or four strongest findings, where the report was saved, and the one next step you recommend. Offer to do it.

Follow the evidence skill for the scripts and rules. Its folder is next to this one. Its five rules apply to everything below.

## Getting the data

Work down this list and stop at the first that applies.

1. **A connected tool.** If you have a tool that can return the full text of calls, tickets or conversations, use it. Prefer tools that return the actual transcript or messages over ones that return a summary or an answer. Ask for every page of results, since many return only a handful by default. Only read; never update or close anything. Save what you fetch into `research/transcripts/`.
2. **An export.** Ask for it by name, because the obvious export is often empty of customer words. `references/getting-the-data.md` lists what to ask for from the common tools.
3. **A folder, files or pasted text.** Use them as they are.

## Steps

1. **Prepare.** Run `prepare.py` on the input. If it warns that an export has no customer text, stop and tell the user exactly which export to get.
2. **Tell the user what you have.** The number of documents, the scale the script reported, and how you will approach it. For a large corpus, say you will start with a sample.
3. **Read the reference file for each source type** in the corpus: `references/tickets.md`, `calls.md`, `surveys.md`, `churn.md`, `win-loss.md` or `reviews.md`. Each says what that source is good for and what it distorts.
4. **Extract.** One document or small batch at a time, write records to `research/voc/evidence.jsonl`. For each thing a customer said that matters, record the verbatim quote, a `kind`, the `source` type, and a short `note`. Do not assign themes yet.
5. **Verify.** Run `verify_quotes.py`. Fix or drop every record that fails.
6. **Draft themes from a sample.** Read up to about fifty verified records spread across sources. Propose 8 to 15 themes named in the customers' words, each with a one-line definition and an example. Show them to the user and ask what to rename, merge or split. This is the step where their judgement adds most.
7. **Fix the themes.** Save them to `research/voc/themes.md`. Then give every record a `theme` from that list, using `other` when nothing fits. If `other` passes about a tenth of the records, a theme is missing; add it and recode.
8. **Count.** Run `count.py --by theme`, and again with `--split source`.
9. **Write the report.**

### Kinds

Use these for `kind`, plus the four forces when a customer describes a switch:

`problem`, `request`, `workaround`, `praise`, `question`, `cancel-reason`, `switch`, `push`, `pull`, `anxiety`, `habit`

A `workaround` is the most valuable kind. It shows someone cared enough to build their own fix.

## Scale

| Corpus | Approach |
| --- | --- |
| Up to about 10 transcripts or 300 short items | Read directly. Still extract, verify and count. |
| Up to about 50 transcripts or 2,000 items | One document or batch of about 25 items at a time, writing records as you go |
| More than that | Draft and fix themes on a sample of a few hundred items first, then work through everything. Use subagents if you have them, each handling a batch, writing to its own file and returning only the file path. |

When the user asks how many, either process everything or say plainly that the figure comes from a sample and give its size.

## The report

Write to `research/voc/report.md`:

```markdown
# What customers are saying
<date> · Based on <n> documents: <breakdown by source>

## What this covers and what it misses
Analysed, skipped and unreadable. Whose voices each source over-represents, and who is absent.

## Themes
| Theme | Documents | Of | By source | What it means |
One section per theme follows, with the definition, two or three verified quotes with participant codes, and what kinds make it up.

## Workarounds
What customers have built for themselves.

## What is different by source or segment
Only differences the counts support.

## Hypotheses
What this suggests, each marked as untested.

## Who to talk to
Five to eight participant codes or accounts whose feedback is worth an interview, why, and what to ask. Offer to write the guide.

## Weak signals
Themes with one or two documents.
```

## Rules

- Themes are named for the customer's problem. "Cannot trust the numbers" is a theme, and "Dashboard improvements" is a feature area.
- Keep what a customer wants (`request`) apart from why they want it. The reason is the finding.
- Do not report a percentage for a theme with fewer than ten documents; give the count.
- When the user arrives with a belief about what the data will show, do the extraction first and compare afterwards. Look for evidence against each theme as well as for it.
- On a later run with new data, keep the existing themes file, code the new records against it, and report what changed. Change the themes only when the user agrees, and then recode everything.
