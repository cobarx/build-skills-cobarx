# 0023. `skill-evals`: measuring a skill's effect is a skill of its own

- **Status:** Accepted
- **Decided:** 2026-10-05 · **Recorded:** 2026-10-05 · Claude Opus 5.5
- **Affects:** `skill-evals` (new)

## Context

Records 0015 to 0018 settled how an eval suite here is built, and at first named no skill. Reviewing
them, the owner asked: "a decision should result in an implementation. is a link sufficient or do
we need to update or add skills to enforce them." An agent writing an eval loads skills by their
triggers, and follows a link only if something it loaded points there.

Other lessons had no home either:

- #10: a suite that only shows a skill loads proves nothing about its effect, and prompts that
  give the answer away score the same with and without the skill.
- The #11 walkthrough (2026-10-03): a case checking the skill stays unloaded needs a near miss, not
  a prompt far from every trigger.
- #61's review: a headline result that didn't reproduce on a rerun (R2), and evidence reported
  after a grader had changed.

## Options

- **A link** from `evals/` to the records. It reaches only someone already reading there.
- **Fold into `definition-of-done`**, whose eval started this. It governs what a change shows a
  reviewer, not how a skill's effect is measured.
- **Fold into `test-fidelity`** (planned). It governs whether a test of code can fail for the real
  reason. Rule 6 here is that idea applied to graders, but the rest is specific to evaluating the
  skills of a library, as `skill-versioning` is specific to versioning one. And it isn't built.
- **A peer skill.**

## Decision

A peer skill, `skill-evals`. The owner chose it (2026-10-05): "1 & 2 are good. we should implement
them. deterministic checks like #2 are great." The name says what is evaluated; `evals` alone
would admit any eval (`naming` rule 2). The owner's separate `skill-evals` repository, a benchmark
of this library against others, is being renamed so the two aren't confused (2026-10-05).

| Rule | Source |
|---|---|
| 1. Score the answer in two arms, with and without, or before and after a change | #10, #61 |
| 2. The prompt does not give the answer away | #10, #61 |
| 3. Check that the skill stays unloaded on a near miss | #11 walkthrough |
| 4. Cases sit under the skill they test | 0015 |
| 5. Each case explains itself in a README | 0016 |
| 6. A grader is seen to fail and to pass | 0017 |
| 7. The judge is a pinned, approved model | 0018 |
| 8. Read the replies, not just the score | 0017's consequences, #61 |
| 9. A result is the run that produced it | #61's review, and its split (#101) |

## Consequences

- Rules 4 to 7 can be checked by a script (#105); until then, in review.
- Rule 7 has no approved judge yet (#99), so every LLM-graded result is provisional until then.
- When `test-fidelity` is built, rule 6 may move to it in a general form.
- Adding a skill is a minor bump.
