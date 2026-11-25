# Brian Rhea's Product Skills

Skills for product people and their agents.

Skills that teach Claude Code, Codex and GitHub Copilot to do market research and Jobs to Be Done: plan interviews, analyze transcripts, find the themes in a pile of tickets and calls, size up the competition, and turn what customers said into job maps, priorities and copy.

You still talk to your customers. The agent does the prep, the synthesis and the first draft.

## Install

<details open>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add brianrhea/skills
claude plugin install brianrhea-skills@brianrhea
```

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add brianrhea/skills
codex plugin add brianrhea-skills@brianrhea
```

</details>

<details>
<summary><strong>GitHub Copilot</strong> (CLI and VS Code)</summary>

```bash
copilot plugin marketplace add brianrhea/skills
copilot plugin install brianrhea-skills@brianrhea
```

</details>

## How to use them

There is nothing to set up. Open your agent in any folder, point it at what you have, and ask.

- "Here's a transcript from yesterday's customer call. What did we learn?" (paste it, attach it or give the path)
- "Analyze the interviews in my Downloads folder."
- "Here are six months of support tickets. What are customers struggling with?"
- "Who are we really competing with? Start from what customers say they used before."
- "Why are people switching to us? Use the interviews so far."
- "Write homepage copy from our research."
- "Draft three onboarding emails for people who just signed up."

Not sure where to begin? Type the front door command. It only runs when you type it:

```
/brianrhea-skills:ask-brian
```

It looks at what you have, tells you where you are in the process and does the next step.

### What the agent keeps for you

Your files stay where they are. The skills save their work in one `research/` folder that the agent creates, so next month's interviews build on this month's:

```
research/
  README.md            where the project stands and what to do next
  context.md           your product, buyer and the decision you are studying
  interview-guide.md
  interviews/          one summary per interview
  corpus/              a cleaned, numbered copy of your raw material, kept out of git
  voc/                 themes, counts and quotes from tickets, calls and surveys
  competitors/         what customers hire instead, and a profile of each competitor
  forces.md
  job-statements.md
  job-map.md
  survey/
  copywriting/         one file per piece: homepage, emails, ads
```

## The skills

Each works on its own. If one needs something an earlier step would have produced, it does that step itself.

| Skill | What it does | Guide |
| --- | --- | --- |
| **Start here** | | |
| [ask-brian](skills/ask-brian/SKILL.md) | Works out where you are, says which skill fits, and does the next step. | [Jobs to Be Done](https://brianrhea.com/jobs-to-be-done/) |
| **Market research** | | |
| [interview-guide](skills/interview-guide/SKILL.md) | Builds a screener and a timeline-based discussion guide for switch interviews. | [Customer research](https://brianrhea.com/customer-research/) |
| [interview-analysis](skills/interview-analysis/SKILL.md) | Summarizes one transcript: timeline, struggling moments and forces, each with a quote. | [Customer research](https://brianrhea.com/customer-research/) |
| [voice-of-customer](skills/voice-of-customer/SKILL.md) | Finds the themes in tickets, calls, survey comments, cancellations and deal notes, with counts and checked quotes. | [Customer research](https://brianrhea.com/customer-research/) |
| [competitive-analysis](skills/competitive-analysis/SKILL.md) | Maps what customers hire instead, then profiles competitors from what they publish, with a source for every claim. | [Customer research](https://brianrhea.com/customer-research/) |
| **Find the pattern** | | |
| [forces-of-progress](skills/forces-of-progress/SKILL.md) | Combines interviews into one ranked push, pull, anxiety and habit diagram. | [Forces of Progress](https://brianrhea.com/forces-of-progress/) |
| [job-statements](skills/job-statements/SKILL.md) | Drafts functional, emotional and social job statements and reviews them. | [Jobs to Be Done](https://brianrhea.com/jobs-to-be-done/) |
| **Decide what to build** | | |
| [job-map](skills/job-map/SKILL.md) | Maps a job across the eight universal steps with outcome statements. | [Job maps](https://brianrhea.com/job-map/) |
| [outcome-survey](skills/outcome-survey/SKILL.md) | Writes an importance and satisfaction survey, then scores the responses. | [Jobs to Be Done](https://brianrhea.com/jobs-to-be-done/) |
| **Put it to work** | | |
| [copywriting](skills/copywriting/SKILL.md) | Writes homepages, emails, ads and onboarding copy from your research, with the source beside each line. | [Website copy](https://brianrhea.com/website-copy/) |
| **Under the hood** | | |
| [evidence](skills/evidence/SKILL.md) | The scripts and rules the others share: quote checking, counting and participant codes. | |

## Every quote is checked by a script

Agents rarely invent a quote. They get roughly one in ten slightly wrong: a word changed, two remarks merged, or the interviewer's question passed off as the customer's answer. You cannot spot those by reading.

So the skills copy quotes into a simple record, and a script checks each one word for word against what a customer actually said. Counts come from a script too, always with what they are out of. Anything that fails is fixed or dropped before you see it.

The scripts need Python 3 and nothing else. Without it, the agent checks by hand and marks the output "Not script-verified".

Findings from tickets, reviews and public pages are treated as hypotheses. The skills end by naming who to talk to, because a pile of feedback tells you what people complain about, and only a conversation tells you why they bought.

## License

MIT
