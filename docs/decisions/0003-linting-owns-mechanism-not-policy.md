# 0003. `linting` owns the mechanism, not the policy

- **Status:** Accepted
- **Decided:** 2026-09-20 (#1) · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** `linting` (planned), and every skill whose rules it enforces

## Context

Several skills need rules enforced mechanically: `simplicity`'s thresholds, `naming`'s denylist,
`contracts`' import boundaries and documentation presence. Someone has to own each threshold and
its reasoning.

## Options

- **`linting` owns the rules it runs**: thresholds, rationale and enforcement in one skill.
- **`linting` owns only the mechanism**: each rule it runs belongs to the skill that requires it.

## Decision

Mechanism only. Every rule `linting` runs is required by another skill, which owns the threshold
and the rationale (`simplicity`: "`simplicity` sets these; `linting` enforces them"). The general
form is a CLAUDE.md convention: do not give a skill policy that belongs to another.

The weighing behind this was not written down at the time; #1 notes it "exists only in
conversation". What the repo does record: a first draft of `linting` was rejected for being stances
("errors not warnings") rather than procedures.

## Consequences

- `linting` is planned as a selection procedure plus an enforcement table that names, for each
  lint, the skill owning the rule it enforces (`docs/context/planned-skills.md`).
- Until `linting` exists, the skills that defer to it are enforced in review.
