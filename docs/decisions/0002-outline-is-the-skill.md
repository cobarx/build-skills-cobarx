# 0002. The outline is the skill

- **Status:** Accepted
- **Decided:** 2026-09-20 (#1) · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** every skill
- **Narrative:** [The outline is the skill](../essays/outline-is-the-skill.md)

## Context

The skills to be ported from MetanoiaFramework ran 300 to 800 lines each, about 2,200 combined:
not reviewable. A skill loads into context every time it fires, and `simplicity` fires on every
unit of work, so its length is a tax on all of them.

## Options

- **Port the documents** as they are.
- **Ship the outline**: `simplicity` outlined at about thirty lines.
- **Expand the outline** into a full skill: tried, at about seventy-five lines.

## Decision

SKILL.md holds rules and nothing else. Bulky material that is still needed lives in `references/`
and `templates/`, loaded on demand; rationale lives in `docs/essays/`. The method is **draft long,
then keep only what is a rule**: the expansion bought exactly two rules the outline had missed (the
exceptions clause and the invented-abstraction caveat), and everything else restated them. Shipping
the long draft is the mistake; never writing it is a quieter one.

## Consequences

- Ports are extractions, not trims.
- Every line answers one test: does this change what anyone does?
- Reasoning cut from a skill moves to an essay or `references/`; it is not deleted (see 0009).
