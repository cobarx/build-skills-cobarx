# 0024. `skill-evals`: a judge is pinned by its model alone

- **Status:** Proposed. Extends [0018](0018-skill-evals-judges-are-pinned-and-qualified.md) (what
  the pin leaves out, and what triggers qualification).
- **Decided:** not yet · **Recorded:** 2026-10-05 · Claude Opus 5.5
- **Affects:** `skill-evals` (rule 7)

## Context

0018 pins the judge by its full model ID. Hampton asked (2026-10-05) whether the model's name and
version are enough, and how much the effort level matters.

For the model, the ID is enough. Anthropic's models overview: "Every Claude model ID is a pinned
snapshot, including the dateless IDs used from the 4.6 generation on."

Three more inputs shape a verdict, and the runner sets all three:

- **Effort**, how much the judge reasons before a verdict. The default differs by model (`high` on
  Sonnet 5.5, `medium` on Opus 5.5).
- **The judge's prompt**, which wraps each grader.
- **The vote:** three votes, and the majority decides.

Checked 2026-10-05 with Claude Code 2.1.289, on #101's known-good control, one run each:

- `claude plugin eval` has no flag for the judge's effort, and its result file records none.
- Effort set to `low` and to `max`, by a project `effortLevel` setting and by `CLAUDE_EFFORT`: the
  judge cost $0.024 every time. Whoever runs the eval doesn't change the judge's effort.
- The result file records the runner version (`claudeVersion`).

## Options

- **Pin effort too.** Not possible: the runner exposes no control for it.
- **Pin the runner as well,** and requalify on each Claude Code version. It updates often, and
  each update would mean a qualification run.
- **Pin the model alone.** Qualify when the model changes, and leave the runner's settings to the
  runner.

## Decision

The model alone. Hampton's call (2026-10-05): qualification runs on a model update, and validating
across Claude Code versions isn't a concern.

- An approval names the model ID. It also records the Claude Code version it was qualified on, for
  reference, not as part of the pin.
- Effort, the judge's prompt and the vote are not pinned. A new Claude Code version does not
  trigger qualification.

## Consequences

- The controls (0017) run with every reported result, so a runner change that breaks the judge on
  clean answers shows there. One that shifts verdicts on borderline replies does not.
- Revisit if a control misbehaves after a Claude Code update, or if replies read under rule 8
  disagree with the judge.
