---
name: spec
description: This skill should be used when asked whether or how something can be done; when about to recommend, compare, or propose a tool, library, rule, heuristic, model, or design, in conversation as much as in code; when handed a choice between options; when starting a project or a unit of work; or when it is unclear how much of the behaviour to pin down. It governs defining what the system must do, and how deeply, before choosing how.
---

# spec

Say what the system must do before choosing how.

A solution proposed before its criteria is a guess dressed as an answer. The spec holds the target
(what the change must accomplish, and what it is judged against), kept current as the owner finds
it, so a choice can be weighed instead of picked.

## Rules

1. **What before how.** Write what the change must do, and the criteria it is judged against, before
   choosing a tool, a library, or a design. Options offered before the criteria are unframed work.
   A question asked as a how ("can we", "which is better") still needs its what before an answer.
   Exploring to find the what is not choosing the how: data, spikes and prototypes answer open
   questions, and what they turn up is a hypothesis until the goal says it fits.

2. **The goal comes from its owner, often in pieces.** When it is not stated, ask the person whose
   problem it is; do not fill it with the convenient reading. Many owners find the goal by
   exploring, so ask what the next step depends on, and do not hold the work for a full answer.

3. **Keep a working goal where both can see it.** A draft, the open questions beside it, and each
   answer recorded, dated, as it lands. Work proceeds against the current draft; an inferred part
   stays marked as a guess until the owner confirms it. When the goal moves, recheck the criteria,
   decisions and work that rested on the earlier draft rather than carry them forward.
   An overall goal can hold while smaller goals beneath it are explored, met and replaced; each
   step is judged against its own goal and must still serve the one above it.

4. **The goal is what the output lets its user do.** Not what it is (a role: "a clip captions
   play against") nor a number it hits (an exact byte count). A goal refined by what was learned
   about the problem is the process working; one fitted to what was built passes by construction.

5. **Specify the class, not the instance.** Name the general problem the case in hand belongs to,
   and write the spec for that. A fix fitted to the instance, such as a pattern that matches the
   samples on hand, is a hypothesis about the class to test, not the solution.

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
