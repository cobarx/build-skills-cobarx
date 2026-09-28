# 0014. License the text under CC BY 4.0; code takes a software licence

- **Status:** Proposed. Accepted once the owner has read the licence and its commentary.
- **Decided:** 2026-09-28 · **Recorded:** 2026-09-28 · Claude Opus 5.5
- **Affects:** every file; how others credit what they copy or adapt

## Context

The repo is being prepared for release and has no licence, so no one may legally reuse it. It is
all Markdown and JSON today; an evals suite with scripts is in progress.

The choice was worked through on 2026-09-25, in the owner's working notes. What decided it:

- **A licence governs copies of the text, not the practice.** Ideas and methods are not
  copyrightable (17 U.S.C. §102(b)), so anyone who rewrites a skill in their own words owes
  nothing under any licence. Copyleft has little to hold in a skill.
- **What the owner wants is credit.** In his words: "You want to establish derivation by
  citation." CC BY §3(a) requires credit with a link to the source and a note of changes; asking
  someone to cite you is the remedy itself, and the 4.0 cure period (§6(b)) makes that ask a
  correction, not a threat. MIT and BSD require only a pasted notice, with no link back.
- **Creative Commons does not recommend its licences for software.** They say nothing of source
  code or patents.

## Options

- **AGPL, with a CLA.** The earlier direction for MetanoiaFramework. Buys friction and no
  protection for a method; no skills repository surveyed uses it.
- **MIT or Apache-2.0.** The ecosystem's usual choice for skills. Treats a skill as a software
  component; credit is a notice, not a citation.
- **CC BY-SA 4.0.** Keeps every later adaptation under the same terms, so the whole chain of
  credit survives, not only the original. Heavier on everyone who adapts.
- **CC BY 4.0.**

## Decision

CC BY 4.0 for the skills and documentation, copyright Hampton Maxwell. Code (the evals, when they
land) takes a software licence, chosen in the PR that adds the first code and stated where the
code lives.

`LICENSE` is the verbatim legal code from creativecommons.org. `plugin.json` declares `CC-BY-4.0`,
its SPDX identifier. The README says how to credit a skill: title, author, source, licence, and
what was changed (Creative Commons' TASL, plus §3(a)'s note of changes).

## Consequences

- The licence is irrevocable for any copy already shared. Going public is the one-way door; adding
  the licence to a private repo is not.
- Much of this repo was written by agents. Text without human authorship may not be copyrightable
  (US Copyright Office, *Copyright and Artificial Intelligence, Part 2*, 2025), which limits what
  attribution can bind. The owner's selection, arrangement, and edits remain protected.
- Skills do not yet carry the licence in their frontmatter (the Agent Skills spec's `license`
  field). A skill copied out of the repo carries no notice until they do. Open.
