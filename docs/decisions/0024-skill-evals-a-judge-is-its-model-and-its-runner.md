# 0024. `skill-evals`: a judge is pinned by its model and its runner

- **Status:** Proposed. Amends [0018](0018-skill-evals-judges-are-pinned-and-qualified.md) (what an
  approval names, and when a judge is checked again).
- **Decided:** not yet · **Recorded:** 2026-10-05 · Claude Opus 5.5
- **Affects:** `skill-evals` (rule 7)

## Context

0018 pins the judge by its full model ID. Hampton asked (2026-10-05) whether the model's name and
version are enough, and how much the effort level matters.

For the model, the ID is enough. Anthropic's models overview: "Every Claude model ID is a pinned
snapshot, including the dateless IDs used from the 4.6 generation on."

For the judge, it isn't. Three more inputs shape a verdict, and the runner sets all three:

- **Effort**, how much the judge reasons before a verdict. It matters most on borderline replies,
  where Haiku erred in #61. The default differs by model (`high` on Sonnet 5.5, `medium` on Opus
  5.5), and the levels were recalibrated between Sonnet 5 and Sonnet 5.5, so a level does not mean
  the same judge across versions.
- **The judge's prompt**, which wraps each grader.
- **The vote:** three votes, and the majority decides.

Checked 2026-10-05 with Claude Code 2.1.289, on #101's known-good control, one run each:

- `claude plugin eval` has no flag for the judge's effort, and its result file records none.
- Effort set to `low` and to `max`, by a project `effortLevel` setting and by `CLAUDE_EFFORT`: the
  judge cost $0.024 every time. Whoever runs the eval doesn't change the judge's effort.
- The result file records the runner version (`claudeVersion`).

## Options

- **Pin effort too.** Not possible: the runner exposes no control for it.
- **Run evals only on an approved runner version.** Claude Code updates itself often, and each
  update would stop every eval until a new approval.
- **Name the runner version in the approval, and recheck cheaply when it changes.**

## Decision

An approval names the model ID and the Claude Code version it was qualified on. The pair is the
judge.

When the runner version changes, rerun qualification step 2 alone: the labelled replies cost only
judge calls, with no agent runs. If every label still matches, the approval carries over to that
version, and the passing result is committed beside the approval's other evidence. If any label
fails, the approval is suspended for that version, and its results don't count, until a full
qualification passes.

Effort is not pinned or recorded on its own: the runner sets it, so the runner version carries it.
If the runner gains a control for the judge's effort, effort joins the pin.

## Consequences

- An approval's evidence grows by one result per runner version checked. The record itself is not
  edited; the results beside it, named by runner version, show where it holds.
- A reported result names its runner version, which `skill-evals` rule 9 already requires.
- #99's qualification command can run step 2 on its own.
