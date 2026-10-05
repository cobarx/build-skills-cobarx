---
name: spec
description: This skill should be used when asked whether or how something can be done; when about to recommend, compare, or propose a tool, library, rule, heuristic, model, or design, in conversation as much as in code; when handed a choice between options; when starting a project or a unit of work; or when it is unclear how much of the behaviour to pin down. It governs defining what the system must do, and how deeply, before choosing how.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills-cobarx/tree/main/skills/spec"}
---

# spec

Say what the system must do before choosing how.

A solution proposed before its criteria is a guess dressed as an answer. The spec holds the target
(what the change must accomplish, and what it is judged against), kept current as the owner finds
it, so a choice can be weighed instead of picked.

## Rules

1. **What before how.** Write what the change must do, and its criteria, before choosing a tool, a
   library, or a design; options offered first are unframed work. A "can we" or "which is better"
   still needs its what. Exploring to find the what is not choosing the how: what data, spikes and
   prototypes turn up is a hypothesis until the goal says it fits.

2. **The goal comes from its owner, often in pieces.** Ask the person whose problem it is; don't
   fill the gap with the convenient reading. Ask what the next step depends on, and keep working
   without the rest.

3. **Keep a working goal where both can see it.** A dated draft, open questions beside it, answers
   recorded as they land; an inferred part stays marked as a guess until confirmed. When it moves,
   recheck what rested on the old draft. A product goal holds while its features go through
   discovery; each feature is judged by its own goal and must serve the product's.

4. **The goal is what the output lets its user do.** Not what it is (a role: "a clip captions
   play against") nor a number it hits (an exact byte count). Refining it by what was learned is
   the process working; fitting it to what was built passes by construction.

5. **Specify the class, not the instance.** Spec the general problem the case belongs to. A fix
   fitted to the samples on hand is a hypothesis about the class, not the solution.

6. **Criteria come from the goal.** They are what `definition-of-done` checks against, and what a
   `decision-log` entry weighs an option by. No goal, no criteria, no spec.

7. **Spec what would be gotten wrong if left unsaid.** Not every behaviour, not just the
   architecture. What the builder gets right from convention can rest on convention; what bears on
   the goal, reads two ways, or would be filled with the convenient guess must be written.

8. **Set the depth by the cost of a wrong guess, and by the builder.** The more a bad guess costs
   (safety, an irreversible action, a builder who builds exactly and only what is written, like a
   vendor or an agent), the closer to exhaustive. A builder who fills gaps with judgement needs less.

9. **Complete when it cannot be met while missing the goal.** If someone could satisfy the whole
   spec and still miss the point, it has a hole; if a line could be cut and nothing would be gotten
   wrong, it is over-specced.

## Not here

Registering the terms a spec uses (the vocabulary chain, industry to code) is `glossary`
(planned); binding code to those terms is `naming`. Whether the goal was met is `definition-of-done`.
How a choice among options is made and recorded is `decision-log`. Understanding the problem and the
evidence behind a goal is the planned *why* skill. This governs what the system must do, and how
deeply, not how it is built.

---

Decisions affecting this skill: `docs/decisions/*-spec-*.md`
