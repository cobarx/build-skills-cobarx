# 0008. Three documentation classes, not two

- **Status:** Accepted
- **Decided:** 2026-09-20 (#1) · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** `durable-context`, `essays`, `decision-log`
- **Narrative:** [The outline is the skill](../essays/outline-is-the-skill.md), "A note on this
  format"

## Context

Skills keep rules only (0002), so the reasoning behind them needs a home, alongside what has been
settled and what is still open.

## Options

- **Two classes**: decision records carrying their own reasoning, plus open questions.
- **Three classes**: terse, dated decision records; essays for the narrative, one per idea; and
  context for what is still open.

## Decision

Three. Decisions and reasoning do not map one to one: one insight drives several decisions, one
decision has several independent reasons, and some reasoning is a lesson that precedes any decision
at all. Forcing that into a decision record flattens it. The part that earns the essay is **what it
cost**, which a terse record always drops and which stops someone undoing the decision later.

## Consequences

- `durable-context` rule 5 names the three homes: `docs/decisions/`, `docs/essays/`,
  `docs/context/` (#42).
- Records point to essays for narrative rather than carrying it.
- `docs/essays/` is a coinage (0006), still open to a better name.
