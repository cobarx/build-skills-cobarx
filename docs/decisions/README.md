# Decisions

What has been settled, one record per decision: terse, dated, append-only. The narrative behind a
decision lives in [docs/essays/](../essays/); what is still open lives in
[docs/context/](../context/).

Records follow [MADR](https://adr.github.io/madr/): `NNNN-title-with-dashes.md`, numbered in order
and never reused. The title starts with the name of each skill the decision governs, so the glob at
the foot of a skill (`docs/decisions/*-<skill>-*.md`) finds it; a library-wide decision names no
skill. A reversed decision gets a new record, and the old one is marked superseded. See 0001.

| # | Decision | Status |
|---|---|---|
| [0001](0001-decision-log-durable-context-record-decisions-as-madr.md) | Record decisions as numbered MADR files | Accepted |
| [0002](0002-outline-is-the-skill.md) | The outline is the skill | Accepted |
| [0003](0003-linting-owns-mechanism-not-policy.md) | `linting` owns the mechanism, not the policy | Accepted |
| [0004](0004-definition-of-done-simplicity-kept-apart.md) | `definition-of-done` stays apart from `simplicity` | Accepted |
| [0005](0005-simplicity-essential-and-accidental-complexity.md) | Brooks's essential and accidental complexity, not a coinage | Accepted |
| [0006](0006-glossary-industry-terms-over-coinage.md) | Industry terms over our own | Accepted |
| [0007](0007-review-adversarial-stance-is-not-a-skill.md) | The adversarial stance is not a skill | Accepted |
| [0008](0008-durable-context-essays-three-documentation-classes.md) | Three documentation classes, not two | Accepted |
| [0009](0009-seventy-line-limit.md) | No skill runs past seventy lines | Accepted |
| [0010](0010-platform-correctness-look-for-a-standard-before-inventing-one.md) | Look for a standard before inventing one | Deprecated |
