# 0016. `skill-evals`: each case explains itself in a README

- **Status:** Proposed
- **Decided:** 2026-10-03 · **Recorded:** 2026-10-03 · Claude Opus 5.5
- **Affects:** `skill-evals` (planned), which carries the rule to every eval suite under `evals/`

## Context

Reviewing #11 on 2026-10-03, the owner asked whether, with only a case's files, an engineer could
tell what the case was for, how it would behave, or when to update it. They couldn't. A PR
description doesn't fix that: it isn't where the next engineer looks.

## Options

- **The `description` field in `prompt.md`'s front matter.** This is the runner's own field. It's
  one line, enough for purpose but not for behaviour or when to update.
- **A `README.md` per case.** It renders on GitHub, and anyone opening the directory reads it. The
  runner ignores it (checked in #61: a run after adding one found the same case and graders).
- **Searched for a standard** on 2026-10-03, with two web searches: one for test case
  specification fields, one for conventions documenting LLM eval cases.
  - **The first** found ISO/IEC/IEEE 29119-3, whose test case specification has four fields:
    objective, preconditions, inputs and expected results. The whole standard is built for
    formal test plans and is heavier than one eval needs.
  - **The second** found no convention for documenting a single eval case, only grader-design
    guidance and framework docs.

## Decision

Every case has a `README.md` with three sections. They adopt part of 29119-3, renamed for readers
who won't know the standard:

- **Purpose** (29119-3's objective): the question the case answers, and why it matters.
- **How it behaves** (its preconditions and inputs): what is sent, what each grader checks, how
  to read the result, and the command to run it.
- **When to update.**

The rest of 29119-3 is left out. The front matter's `description` stays one line and points to the
README.

Example, for a small case. It is illustrative: the case is one #11 plans, not yet built. A full one
is #61's `evals/definition-of-done/plot-signups-pr-description/README.md`.

```markdown
# test-assertions-quiet

An eval case for the `definition-of-done` skill.

## Purpose

Does `definition-of-done` stay unloaded on a near miss? The prompt asks which assertions a unit
test should make. That is close to the skill's triggers, but its description says it governs
"what a change shows, not what its tests assert". A skill that loads here would load on almost
anything, and the cases that check it loads would prove nothing.

## How it behaves

`claude plugin eval` sends `prompt.md` to a fresh agent with this repo's skills installed.
`graders/skill-quiet.md` passes a run only if the agent never calls `Skill` to load
`definition-of-done` (`min: 0`, `max: 0`). Run it from the repo root:

    claude plugin eval . --case test-assertions-quiet

## When to update

- **The skill's `description` changes.** That text decides when the skill loads. Rerun, and check
  the prompt is still a near miss rather than a trigger.
```

## Consequences

- A case's command is written in its README and has to work exactly as written.
