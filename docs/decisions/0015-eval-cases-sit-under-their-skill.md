# 0015. Eval cases sit under the skill they test

- **Status:** Proposed
- **Decided:** 2026-10-03 · **Recorded:** 2026-10-03 · Claude Opus 5.5
- **Affects:** every eval suite under `evals/` (library-wide; names no skill)

## Context

The first eval suite (#11) put each case at `evals/<case>/`, and #47 already points at it as the
format for later suites. With some twenty skills, flat case names collide and don't say which
skill they test. Any layout has to run under `claude plugin eval` without configuration.

## Options

- **Flat `evals/<case>/`.** This is what `claude plugin eval init` creates, so it's the runner's
  convention. It says nothing about grouping cases in a plugin with many skills.
- **`evals/<skill>/<case>/`.** The runner finds cases with `evals/**/prompt.md`, so nesting needs
  no configuration (checked in #61: cases nested this way were found and run).

## Decision

Cases live at `evals/<skill>/<case>/`. Files shared by one skill's cases, such as a capture
script, sit in `evals/<skill>/`.

## Consequences

- #47's cases, and the rest of #11's, use this layout when they're built.
- `--case` matches a case's `name`, not its path, so names must stay unique across every
  skill's suite. Nothing enforces this, so a new case's name is checked against the others.
