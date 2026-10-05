---
name: skill-evals
description: This skill should be used when writing or changing an eval case for a skill; when a change to a skill claims to change what an agent does; when an eval result is about to be reported; or when choosing the model that judges an eval's graders. It governs how a skill's effect on an agent is measured, not what the skill says.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills-cobarx/tree/main/skills/skill-evals"}
---

# skill-evals

Show that a skill changes what an agent does, with a measurement that could have shown it didn't.

A skill that loads and changes nothing costs context every time it fires. The eval is the only
place its effect is seen, so an eval that cannot fail is worse than none: it reads as proof.

## Rules

1. **Score the answer in two arms:** with the skill and without it, or, for a change to a skill,
   before the change and after. That the skill loaded is an indicator, not the score. The claim is
   the difference between the arms.

2. **The prompt does not give the answer away.** A prompt that names what good looks like scores
   the same in both arms. If the arm without the skill already scores full marks, the case is
   broken, not passed.

3. **Check that the skill stays unloaded on a near miss.** Use a prompt close to a trigger in the
   description. One far from every trigger shows nothing.

4. **Cases sit under the skill they test,** at `evals/<skill>/<case>/`, each name unique across
   every suite.

5. **Each case explains itself in a README:** Purpose, How it behaves (including the command to
   run it, which works exactly as written), and When to update.

6. **A grader is seen to fail and to pass before its results count.** Every case with LLM graders
   ships a known-bad control, expected to score 0, and a known-good one, expected to score 1.0,
   sharing the case's graders by symlink. A result counts only when both behave.

7. **The judge is a pinned, approved model.** Name it by its full model ID, never an alias. It is
   approved only by passing the qualification, recorded with the passing result; a new version of
   an approved model is unapproved.

8. **Read the replies, not just the score.** Controls are clean answers; real replies are not.
   Read a sample from every run you report, and report where you and the judge disagree.

9. **A result is the run that produced it.** State the commit, runner version, judge, runs per
   arm, and both arms' scores, and hand over the replies. A grader changed after the run voids
   the result; rerun before reporting. An effect seen once is reproduced before it is claimed.

## Not here

Whether the skill's rules are the right ones is that skill's own. Showing a result to a reviewer
is `definition-of-done`. Where captured replies come from is `fixtures`. Checking cases against
these rules by machine is `linting` (planned). Whether a test in general can fail for the real
reason is `test-fidelity` (planned); this applies it to evals of skills.

---

Decisions affecting this skill: `docs/decisions/*-skill-evals-*.md`
