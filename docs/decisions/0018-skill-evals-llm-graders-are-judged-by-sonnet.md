# 0018. `skill-evals`: LLM graders are judged by Sonnet

- **Status:** Proposed
- **Decided:** 2026-10-04 · **Recorded:** 2026-10-04 · Claude Opus 5.5
- **Affects:** `skill-evals` (planned), which carries the rule to every eval suite under `evals/`

## Context

`claude plugin eval` judges `llm` graders with Haiku unless `--judge-model` says otherwise. On #61's
first case (a private project's clip, since replaced by the signups chart), Haiku passed both
controls, but on real replies it erred both ways. It failed a description containing "[Attach the
generated clip…]", which the grader explicitly accepts, and it passed a description that never asked
for the clip.

## Options

- **Haiku, the default.** Cheapest, and needs no flag. It misjudged real replies, as above.
- **Sonnet.** Rerun on the same commit, its verdicts on providing the clip matched the author's
  reading of all six descriptions, and both controls still behaved. It costs more per run (on that
  case, $0.87 against $0.69 with Haiku). #61's replacement case ran under Sonnet too, and its
  controls behaved.
- **Opus.** Not tried. It costs more again, with no failure of Sonnet's to justify it.

## Decision

Each case's README command sets `--judge-model sonnet`.

## Consequences

- A command without the flag silently falls back to Haiku. The README says not to drop it.
- Revisit when the runner's default judge changes, or when a control or a read sample shows Sonnet
  misjudging.
