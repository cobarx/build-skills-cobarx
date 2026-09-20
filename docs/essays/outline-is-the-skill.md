# The outline is the skill

**2026-09-20**

## Where we landed

SKILL.md holds rules and nothing else. No expanded rationale, no worked examples where the rule is
already unambiguous. Material that is bulky but needed lives in `references/` and `templates/`.
The `description` frontmatter is the one exception that still gets care, because it decides
whether the skill loads at all.

## How we got there

The prompt was "start simple and review the text." The skills we were going to port from
MetanoiaFramework run 300 to 800 lines each, about 2,200 combined. That is not reviewable, and
saying so was the first crack in the assumption that a skill is a document.

Then `simplicity` got outlined, at about thirty lines, and Hampton asked: what if that was the
skill.

The argument for yes was immediate and slightly embarrassing. A skill about simplicity running
500 lines refutes itself. Skills load into context every time they fire, and `simplicity` fires on
every unit of work, so its length is a tax on every piece of work in the project. Bounded context
is the thing it teaches.

## The test we ran

I expanded the outline into a full skill anyway, roughly seventy-five lines. Hampton's response
was the useful part: "we went from an outline to a number of explanations. what does this get us."

Going through it honestly, the expansion bought exactly two things, and both were *rules* the
outline had missed:

- **The exceptions clause.** Greenfield first commits, generated code, and mechanical refactors
  are single units regardless of size. Without it the sizing rule fires wrongly on its first real
  encounter and gets switched off.
- **The abstraction caveat.** An abstraction invented to make the one-sentence test pass is a
  failure, not a pass. This closed a loophole I had tried to use one message earlier, when I
  argued that "govern the unit at both ends" was a single concept rather than two.

Everything else was section 4 restating section 2, a paragraph on why bounded context is good, and
a list of what dependencies cost. None of it changed what anyone would do.

## What it cost, and the part worth transferring

Nearly losing two rules.

If we had shipped the outline directly, the exceptions clause would not exist, and `simplicity`
would have been abandoned the first time it fired on a greenfield commit and demanded the
impossible.

So the practice is **not** "write short." It is:

> **Draft long, then keep only what is a rule.**

The long draft is a discovery tool. Write it, go through it line by line, and ask of each one:
*does this change what anyone does?* Keep those. Delete the rest. Shipping the long draft is the
mistake; never writing it is a different and quieter mistake.

## What it shapes

- The ports from MetanoiaFramework are now extractions rather than trims. Pull out the rules, drop
  the prose, move the material to `references/`.
- Every skill written since has come in under sixty lines.
- It is why `platform-correctness` rule 1 needed a scope qualifier and got three lines rather than
  a paragraph. The qualifier was a rule; the paragraph would have been padding.
- It is why this file exists. The reasoning above is real and worth keeping, and none of it
  belongs in a SKILL.md.

## A note on this format

Decisions and reasoning do not map one to one. One insight drives several decisions; one decision
has several independent reasons; some reasoning is a lesson that precedes any decision at all.
Forcing that into an ADR flattens it.

So: `docs/decisions/` stays terse and dated, an index of what is settled. These essays carry the
narrative, one per idea. `docs/context/` holds what is still open.

The section that earns this format is **what it cost**. A terse ADR always drops it, and it is the
part that stops someone undoing the decision later.
