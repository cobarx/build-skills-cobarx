---
name: spec
description: This skill should be used when a change needs a choice about how to build it (a tool, a library, a design); when work jumps to a solution before what it must do is written down; or when it is unclear how much of the behaviour to pin down. It governs defining what the system must do, and how deeply, before choosing how.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills-cobarx/tree/main/skills/spec"}
---

# spec

Say what the system must do before choosing how.

A solution proposed before its criteria is a guess dressed as an answer. The spec fixes the target
(what the change must accomplish, and what it is judged against), so a choice can be weighed
instead of picked.

## Rules

1. **What before how.** Write what the change must do, and the criteria it is judged against, before
   naming a tool, a library, or a design. Options offered before the criteria are unframed work.

2. **The goal is what the output lets its user do.** Not what it is (a role: "a clip captions
   play against") nor a number it hits (an exact byte count). State it before the work; a goal
   fitted afterward to what was built passes by construction.

3. **Criteria come from the goal.** They are what `definition-of-done` checks against, and what a
   `decision-log` entry weighs an option by. No goal, no criteria, no spec.

4. **Spec what would be gotten wrong if left unsaid.** Not every behaviour, not just the
   architecture. What the builder gets right from convention can rest on convention; what bears on
   the goal, reads two ways, or would be filled with the convenient guess must be written.

5. **Set the depth by the cost of a wrong guess, and by the builder.** The more a bad guess costs
   (safety, an irreversible action, a builder who builds exactly and only what is written, like a
   vendor or an agent), the closer to exhaustive. A builder who fills gaps with judgement needs less.

6. **Complete when it cannot be met while missing the goal.** If someone could satisfy the whole
   spec and still miss the point, it has a hole; if a line could be cut and nothing would be gotten
   wrong, it is over-specced.

## Not here

Registering the terms a spec uses (the vocabulary chain, industry to code) is `glossary`
(planned); binding code to those terms is `naming`. Whether the goal was met is `definition-of-done`.
How a choice among options is made and recorded is `decision-log`. This governs what the system must
do, and how deeply, not how it is built.

---

Decisions affecting this skill: `docs/decisions/*-spec-*.md`
