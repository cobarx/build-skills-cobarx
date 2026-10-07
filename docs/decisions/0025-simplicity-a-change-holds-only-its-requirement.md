# 0025. `simplicity`: a change holds only its requirement

- **Status:** Accepted
- **Decided:** 2026-10-06 (#PR) · **Recorded:** 2026-10-06 · Claude Opus 5.5
- **Affects:** `simplicity`

## Context

A pilot ran plain Claude Code, a 65-line always-loaded CLAUDE.md (Karpathy's four principles) and
this library on 48 MaintainBench requirement changes, twice. With the CLAUDE.md, an agent changing
existing code for a new requirement changed 15.5 fewer lines than with this library (95% CI 12 to
19) and kept more of the code's structure. Pass rates did not differ clearly. The diffs showed
where the extra lines came from: unchanged logic extracted into helpers, closures turned into
classes, and validation, exception hierarchies and fallbacks nobody asked for. Nothing here said
not to. `naming` 7 (a rename is its own change) and `format` 3 (a reformat lands alone) cover two
cases of the rule, and `simplicity` 8 named only documentation and tests.

## Options

- **A new skill.** Rejected: the rule keeps a change cheap to review, which is `simplicity`'s one
  sentence.
- **Extend `naming` 7 and `format` 3.** Rejected: they are cases of a cross-cutting rule, and the
  rule is their peer, not part of either.
- **Widen `simplicity` 8 and add a rule beside it.** 8 is about producing things nobody asked for;
  the new rule is about changing what is already there.

## Decision

Rule 8 lists validation, error types, fallbacks, special cases and compatibility shims beside
documentation and tests. New rule 9, *Touch only what the requirement reaches*: a change to
existing code holds that requirement and nothing else, new behaviour goes where the old lives in
the style already there, and a needed restructuring is its own unit, landed first.

## Consequences

- `simplicity` grows from 58 to 64 lines.
- Rule 9 sits beside rule 5 (*Extract, do not raise the threshold*): extracting to meet a threshold
  is still right, but as its own unit, not inside a behaviour change.
- In the pilot no skill in this library loaded on its own; only descriptions were in context. These
  rules change what an agent does once `simplicity` loads. Whether it loads is a separate change.
