---
name: simplicity
description: This skill should be used before starting any unit of work; when a task or PR description needs the word "and" to be accurate; when a function grows a third level of nesting; when a new dependency is proposed; when a complexity gate fails; or when asked to do several things at once. It bounds how much rides in a single unit of work, so that any one part can be built, changed, or reviewed with only its contract in view.
---

# simplicity

Bound the size of a unit of work. Small units keep the working context bounded, so any part can be
built, changed, or reviewed with only its contract in view.

## Rules

1. **One sentence, no "and".** If you cannot describe the unit in one sentence without "and", it is
   more than one unit. An abstraction invented to make the sentence work is a failure, not a pass.

2. **Cross-cutting concerns are peers.** If a thing references three siblings, it belongs beside
   them, never inside one of them.

3. **Sequence dependencies, do not merge them.** A unit that cannot be built without another is an
   ordering problem.

4. **Exceptions, named so the rule survives.** A greenfield first commit, generated code, and
   mechanical refactors are single units regardless of size. Reviewing them does not require
   holding many things in mind at once.

5. **Extract, do not raise the threshold.** Overriding a default is a decision, and gets logged.

6. **Admit dependencies deliberately.** Review before it enters. Prefer the platform. Prefer twenty
   local lines over a dependency used once.

7. **Propose the split.** When asked for too much at once, say so, and give the units and their
   order. State it once; if reaffirmed, proceed.

## Thresholds

`simplicity` sets these; `linting` enforces them. Cognitive over cyclomatic: cyclomatic counts
branches, cognitive penalizes nesting, which is closer to what a person can hold in their head.

| Measure | Default |
|---|---|
| Cognitive complexity | 15 |
| Nesting depth | 3 |
| Function length | 50 lines |
| File length | 300 lines |
| Parameters | 4 |

These are budgets, not targets. Complexity essential to the problem must be paid for; complexity
introduced by the solution is waste. Being under the threshold is not the same as having earned it.

Completion is not here. See `definition-of-done`.

---

Decisions affecting this skill: `docs/decisions/*-simplicity-*.md`
