# 0007. The adversarial stance is not a skill

- **Status:** Accepted
- **Decided:** 2026-09-20 (#1) · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** `review`, `test-fidelity` (planned), `definition-of-done`, every checkpoint
- **Source:** `docs/context/planned-skills.md`, "The adversarial stance is not a skill"

## Context

Attacking the work (trying to disprove it rather than inspect it) was proposed as a skill of its
own.

## Options

- **A skill for the stance.**
- **No skill**: the stance lands inside the skills that act.

## Decision

No skill. The stance has no procedure of its own, and making it one would repeat the rejected
first draft of `linting`, which was stances rather than procedures (0003). It lands in three places
instead:

- `test-fidelity` rule 5: write the test that tries to break it.
- The shape of every checkpoint: `naming` predicts before reading, `contracts` asks what you had to
  open. Future checkpoints are phrased as an attempt to disprove, never as a review.
- `definition-of-done`'s burden of proof.

The caveat that makes it survivable: scale to blast radius. A rule that fires on everything gets
switched off.

## Consequences

The same note asked for an explicitly invoked mode, since self-review has a ceiling. `review` (#15)
later added a skill for the independent-critic role, with a procedure: take a lens with a named
disproof, report pass, fail or blocked, keep one review of record. It is close to that mode, though
#15 does not cite this decision. The stance itself still has no skill.
