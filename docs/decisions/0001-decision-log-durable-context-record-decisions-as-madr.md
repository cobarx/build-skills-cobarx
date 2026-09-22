# 0001. Record decisions as numbered MADR files

- **Status:** Accepted
- **Decided:** 2026-09-22 · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** `decision-log` (the form of a record), `durable-context` (where it lives)

## Context

Every skill ends with the glob `docs/decisions/*-<skill>-*.md`, and the directory did not exist.
#42 settled the location (`durable-context` rule 5) and left the filename scheme to the first
record. A scheme must let each skill's glob find what governs it, give every record a stable id to
supersede by, and follow an industry convention rather than a coinage (0006).

## Options

- **Nygard ADRs**: `doc/arch/adr-NNN.md`, sections Title, Context, Decision, Status, Consequences
  ([Nygard, 2011](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).
- **MADR**: `docs/decisions/NNNN-title-with-dashes.md`, with context, considered options, outcome
  and consequences ([MADR](https://adr.github.io/madr/)).
- **Date-prefixed files** (`YYYY-MM-DD-<slug>.md`): the first seven records were all decided on
  2026-09-20, so dates give no order and no stable id.

## Decision

MADR: its directory is the one `durable-context` already names, and its sections carry the options
weighed, which `decision-log` rule 2 requires. Records stay terse. The title after the number starts
with the name of each skill the decision governs, so `*-<skill>-*` finds it; a library-wide
decision names no skill and is found from the index. Numbers are never reused. A reversed decision
gets a new record, and the old one's status becomes "Superseded by NNNN", the only edit an accepted
record takes (Nygard).

## Consequences

- Slugs avoid skill names except as those leading tags: `*-spec-*` would match a slug that merely
  says "spec".
- `README.md` in this directory indexes every record.
- Where the original weighing was never written down, a record says so rather than reconstruct it
  as fact.
