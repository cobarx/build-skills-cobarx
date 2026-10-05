# 0017. An LLM-graded eval case ships a known-bad and a known-good control

- **Status:** Proposed
- **Decided:** 2026-10-03 · **Recorded:** 2026-10-03 · Claude Opus 5.5
- **Affects:** every eval suite under `evals/` (library-wide; names no skill)

## Context

In #11, and in the first version of #61, every `llm` grader had only ever been seen to pass.
Full marks with and without the skill is also what a grader that passes anything would produce.
Adding only a known-bad answer wasn't enough either: in #61 a judge then failed a description that
did exactly what the grader asked.

## Options

- **A one-off check, described in a PR.** It's lost after merge, and nothing reruns it when a
  grader changes.
- **Control cases in the same suite,** handing the graders fixed answers. They sit beside the case
  and rerun with it. They can share the case's graders by:
  - **copying them,** which lets the two drift apart;
  - **the runner's `case.yaml` format,** which is undocumented;
  - **symlinks,** which keep a single source. The runner follows them (checked in #61: a control
    loaded four linked graders and graded with them).

## Decision

Every case with `llm` graders ships two controls, each named for what it holds (for example
`plot-signups-known-bad/`):

- **A known-bad answer, expected to score 0.** This catches a grader that passes anything.
- **A known-good answer, expected to score 1.0.** This catches a grader that fails good work.

An agent with no tools repeats the answer verbatim. The controls' graders are symlinks to the
case's graders. A result from the case counts only when both controls behave.

## Consequences

- A known-bad control scores 0 by design, so a run that includes one exits with status 1. Run
  cases and controls separately with `--case`.
- The controls are clean, clear-cut answers. They don't show that a grader judges real replies
  consistently, which wrap the answer in commentary and phrase placeholders their own way (#61's
  review of record, F2). Read a sample of real replies as well.
- Symlinked graders need a checkout that keeps symlinks. Git does on Linux and macOS. On Windows,
  symlinks have to be enabled for the clone.
