# simplicity: thresholds

`simplicity` sets these; `linting` enforces them. Cognitive over cyclomatic: cyclomatic counts
branches, cognitive penalizes nesting, which is closer to what a person can hold in their head.

| Measure | Default |
|---|---|
| Cognitive complexity | 15 |
| Nesting depth | 3 |
| Function length | 50 lines |
| File length | 300 lines |
| Parameters | 4 |

These are diagnostics, not targets. A function over fifty lines is not wrong for being long; it is
long because a design decision upstream went wrong, and the number is how you notice.
