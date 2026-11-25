# Brian Rhea's Skills

Skills for product people and their agents.

Seven skills that teach Claude Code, Codex and GitHub Copilot to do Jobs to Be Done customer research: plan the interviews, analyze the transcripts, and turn what customers said into job maps, priorities and website copy.

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

## The skills

Listed in the order you would use them on a project. Each works on its own.

| Skill | What it does | Guide |
| --- | --- | --- |
| [interview-guide](skills/interview-guide/SKILL.md) | Builds a screener and a timeline-based discussion guide for switch interviews. | [Customer research](https://brianrhea.com/customer-research/) |
| [interview-analysis](skills/interview-analysis/SKILL.md) | Summarizes one transcript: timeline, struggling moments and forces, each with a quote. | [Customer research](https://brianrhea.com/customer-research/) |
| [forces-of-progress](skills/forces-of-progress/SKILL.md) | Combines interviews into one ranked push, pull, anxiety and habit diagram. | [Forces of Progress](https://brianrhea.com/forces-of-progress/) |
| [job-statements](skills/job-statements/SKILL.md) | Drafts functional, emotional and social job statements and reviews them. | [Jobs to Be Done](https://brianrhea.com/jobs-to-be-done/) |
| [job-map](skills/job-map/SKILL.md) | Maps a job across the eight universal steps with outcome statements. | [Job maps](https://brianrhea.com/job-map/) |
| [outcome-survey](skills/outcome-survey/SKILL.md) | Writes an importance and satisfaction survey, then scores the responses. | [Jobs to Be Done](https://brianrhea.com/jobs-to-be-done/) |
| [website-copy](skills/website-copy/SKILL.md) | Drafts homepage copy from your research, with the source beside each line. | [Website copy](https://brianrhea.com/website-copy/) |

## How to use them

Put your research in a folder and ask in plain language.

```
research/
  interviews/     transcripts, one file per interview
  analysis/       the skills write their output here
```

Then, for example:

- "Write an interview guide for people who recently switched to our scheduling tool."
- "Analyze the transcripts in research/interviews."
- "Build a forces of progress diagram from those interviews."
- "Create a job map for 'prepare a quarterly board report'."
- "Draft homepage copy from the forces diagram and job statements."

## One rule runs through all of them

Every finding is tied to a quote copied exactly from your research. Anything the agent inferred without a quote is labelled as an assumption. If you see a quote you do not recognize, search the transcript for it.

## License

MIT
