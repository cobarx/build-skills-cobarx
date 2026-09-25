# 0010. Look for a standard before inventing one

- **Status:** Deprecated. Reverted; the review of record on #46 found the rule did not change behaviour and did not belong in `platform-correctness`.
- **Decided:** 2026-09-24 · **Recorded:** 2026-09-24 · Claude Opus 5.5
- **Affects:** `platform-correctness` (new rule 2)

## Context

An agent building a setup helper for agent-memory-cobarx named a per-machine marker file
`.agent-memory`, a coinage. Asked whether it was a convention, it found two draft proposals for a
`.agents/` directory with a memory path, one of which fit, inside a directory real tools already
read. The marker moved there (agent-memory-cobarx 0001).

No skill would have stopped the coinage. `platform-correctness` rule 1 says to look a convention
up, but assumes one is known to exist; it does not say to check before inventing. 0006 (industry
terms over our own) says it for vocabulary only. `simplicity`'s *Weigh dependencies both ways*
covers code taken on, not a format or layout followed. Standards from outside the platform
(MADR, SemVer, AGENTS.md, `.agents/`) fall between all three.

The owner's criteria for adopting one: beneficial, mature, not overly complicated.

## Options

- **Widen 0006** in this repo's CLAUDE.md to all standards. It governs this repo only, so it never
  reaches the projects the skills are loaded into, where the coinage happened.
- **Extend `simplicity`'s dependency rule.** Adopting a standard is not taking on code; a
  different act under a rule about supply chains.
- **A new skill.** One rule does not make a skill, and it would sit beside `platform-correctness`
  with the same spine.
- **A rule in `platform-correctness`.** Its spine, conventions as an interoperability contract,
  holds for community standards too, and its description already triggers on naming things,
  laying out files and hand-rolled equivalents.

## Decision

A rule in `platform-correctness`, placed after *Cite, do not recall* as rule 2: look for a standard
before inventing one, beyond the platform too. The owner's criteria become the test: in real use
(mature), fits what you store (beneficial), costs less to follow than to invent (not overly
complicated). A draft is weighed, not obeyed, and choosing it or coining anyway is logged.

## Consequences

- 0006 stands, as this rule's vocabulary case in this repo; the planned `glossary` keeps
  registering terms.
- Rules 2 to 8 become 3 to 9. Only rule 1 was cited by number elsewhere.
- The skill's one-line purpose still says "the environment the software runs in". A community
  standard is read as part of that environment's ecosystem layer (rule 3), not a new scope.
- Adding a rule is a minor bump: 0.11.0 to 0.12.0.
