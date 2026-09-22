# 0004. `definition-of-done` stays apart from `simplicity`

- **Status:** Accepted
- **Decided:** 2026-09-20 (#1) · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** `definition-of-done`, `simplicity`

## Context

`simplicity` governs the unit of work. Whether a unit is complete is the neighbouring question, and
it could have been a rule there. The decision predates `definition-of-done` itself (#9, 2026-09-21):
the first `simplicity` already said "Completion is not here."

## Options

- **Completion as a rule in `simplicity`.**
- **Completion as its own skill.**

## Decision

Its own skill. `simplicity` points out ("Completion is not here. See `definition-of-done`."), and
`definition-of-done` points back ("Whether the unit is one thing is `simplicity`.").

The weighing was not written down at the time; #1 notes it "exists only in conversation". What the
repo shows is consistent with it: the two purposes, "make every change cheap to understand" and
"done is the goal shown to be met", need an "and" to share one sentence, which is the repo's test
for two skills.

## Consequences

- `simplicity`, which fires on every unit, carries no completion rules.
- `definition-of-done` grew into a skill about goals and evidence (#9, #14, #42) without touching
  `simplicity`.
