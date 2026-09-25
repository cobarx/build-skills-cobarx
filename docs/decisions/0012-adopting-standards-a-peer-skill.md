# 0012. Adopting standards is a peer skill, not a platform rule

- **Status:** Accepted. Supersedes [0010](0010-platform-correctness-look-for-a-standard-before-inventing-one.md).
- **Decided:** 2026-09-24 · **Recorded:** 2026-09-24 · Claude Opus 5.5
- **Affects:** `adopting-standards` (new), `platform-correctness` (a pointer only)

## Context

An agent building a setup helper for agent-memory-cobarx named a per-machine marker file
`.agent-memory`, a coinage. Asked whether it was a convention, it found a draft proposal whose
`.agents/memory` path fit, inside a `.agents/` directory real tools already read, and moved the
marker there ([agent-memory-cobarx 0001](https://github.com/cobarx/agent-memory-cobarx/blob/main/docs/decisions/0001-setup-marker-at-agents-memory.md)).

No skill would have stopped the coinage. `platform-correctness` rule 1 says to look a convention up
but assumes one is known to exist. 0006 (industry terms over our own) covers vocabulary only.
`simplicity`'s *Weigh dependencies both ways* covers code taken on, not a format followed.

The owner asked for existing standards to be used "where appropriate (beneficial, mature, not
overly complicated, etc.)".

## Options

- **A rule in `platform-correctness`** (0010, merged in #46, reverted in #48). An independent
  review ran it headless against main, three runs each: the skill loaded, but no run searched beyond
  the platform, and the outcome did not change. MADR, SemVer and AGENTS.md are not conventions of a
  runtime environment, so the skill's purpose would need an "and".
- **Widen 0006 in CLAUDE.md.** Governs this repo only; never reaches the projects skills load into.
- **Widen the planned `glossary`.** Registering a term is a different act from adopting a format,
  and `glossary` does not exist yet.
- **The planned `project-setup`.** Owns choices made before the first feature, but standards come up
  throughout; the motivating case came mid-project.
- **`platform-correctness` rule 5** (put state where the platform says). Covers where state lives,
  not what to call it or what format it takes; most standards are not state placement.
- **Extend `simplicity`'s dependency rule.** Adopting a standard is not taking on code.
- **A peer skill.** The concern touches `platform-correctness`, `simplicity`, `glossary`,
  `project-setup` and `decision-log`; CLAUDE.md makes a concern that references three siblings
  their peer.

## Decision

A peer skill, `adopting-standards`, with the test built from the owner's criteria and the review's:

- **Benefits** (the owner's *beneficial*): readers that already understand the standard, which is
  interoperability, the reason behind 0006; and thinking done by people with more context, which
  keeps answering questions as the work grows.
- **Costs** (the owner's *not overly complicated*): learning and fitting to it, and leaving it if it
  fades (reversibility, from the review). The best standards are cheap to learn and carry a lot, as
  Markdown and SemVer do.
- **Maturity** (the owner's *mature*) raises both benefits and lowers the risk of leaving. A draft
  is adopted only when leaving is cheap.
- **Audience and lifespan decide the balance** (the owner's). A quick tool for one person may roll its
  own; for a non-technical owner, a standard is one more thing to learn and one more decision to
  understand, and that cost is theirs even when an agent does the fitting.
- **Convergence breaks ties** (from the review), as the repo already says for linters.
- **Partial adoption is declared, and the choice is logged either way** (from the review).

The name is `adopting-standards`, the act it governs. `standards` alone would collide with how
`review` and `simplicity` use the word, for the skills a change is held to.

## Consequences

- `platform-correctness` is unchanged except for a "Not here" pointer.
- 0006 stands, as the vocabulary case in this repo; `glossary` keeps the register act.
- Whether the skill changes behaviour is shown in the PR that adds it, by the same headless
  comparison, and becomes a standing eval in #47.
- Adding a skill is a minor bump.
