# 0025. `simplicity`: a change holds only its requirement

- **Status:** Accepted
- **Decided:** 2026-10-06 (#119) · **Recorded:** 2026-10-06 · Claude Opus 5.5
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

- **A new skill.** Rejected: the rules keep a change cheap to review, which is `simplicity`'s one
  sentence.
- **Extend `naming` 7 and `format` 3.** Rejected: they are cases of a cross-cutting rule, and the
  rule is their peer, not part of either.
- **List what rule 8 forbids** (validation, error types, fallbacks, shims). Tried in the first
  draft of #119; rejected in review: a longer list is more detail, not a clearer rule, and still
  incomplete.
- **Generalise rule 8, and add a scope rule and a style rule beside it.**

## Decision

- Rule 8 says "produce nothing the spec and the standards do not require", in place of naming
  documentation and tests. Its working-notes paragraph, added in #4 after rule 8 was misapplied to
  delete `docs/context/`, becomes one sentence: the rule governs finished output.
- New rule 9, *Touch only what the requirement reaches*: anything else you would improve is its
  own unit, offered, and done only once approved.
- New rule 10, *Adopt the style of finished work*: new work follows an existing finished unit of its
  kind (code, documentation, a spec, a contract), and where that example falls short, it is still
  followed and the cleanup offered under rule 9.

## Consequences

- `simplicity` grows from 58 to 62 lines.
- Rule 9 sits beside rule 5 (*Extract, do not raise the threshold*): extracting to meet a threshold
  is still right, but as its own unit, not inside a behaviour change.
- Rule 10 applies beyond code. Consistency lowers review cost for any artifact.
- In the pilot no skill in this library loaded on its own; only descriptions were in context. These
  rules change what an agent does once `simplicity` loads. Whether it loads is a separate change.
