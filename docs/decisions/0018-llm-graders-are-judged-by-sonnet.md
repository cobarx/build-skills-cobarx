# 0018. Eval cases' LLM graders are judged by Sonnet

- **Status:** Proposed
- **Decided:** 2026-10-04 · **Recorded:** 2026-10-04 · Claude Opus 5.5
- **Affects:** every eval suite under `evals/` (library-wide; names no skill)

## Context

`claude plugin eval` judges `llm` graders with Haiku unless `--judge-model` says otherwise. In #61
Haiku passed both controls, but on real replies it erred both ways. It failed a description
containing "[Attach the generated clip…]", which the grader explicitly accepts, and it passed a
description that never asked for the clip.

## Options

- **Haiku, the default.** Cheapest, and needs no flag. It misjudged real replies, as above.
- **Sonnet.** Rerun on the same commit, its verdicts on providing the clip matched the author's
  reading of all six descriptions, and both controls still behaved. It costs more per run (in #61,
  $0.87 for the case against $0.69 with Haiku).
- **Opus.** Not tried. It costs more again, with no failure of Sonnet's to justify it.

## Decision

Each case's README command sets `--judge-model sonnet`.

## Consequences

- A command without the flag silently falls back to Haiku. The README says not to drop it.
- Revisit when the runner's default judge changes, or when a control or a read sample shows Sonnet
  misjudging.
