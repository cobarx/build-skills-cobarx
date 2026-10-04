# 0019. The evals directory takes Apache-2.0

- **Status:** Accepted
- **Decided:** 2026-10-04 · **Recorded:** 2026-10-04 · Claude Opus 5.5
- **Affects:** everything under `evals/`

## Context

[0014](0014-license-cc-by-4-0.md) licenses the skills and documentation under CC BY 4.0 and leaves
the evals to a decision of their own. An eval case mixes three kinds of file: prose (prompts,
graders, READMEs), data (`case.yaml`, CSVs, scrubbed transcripts), and code (capture and scrub
scripts, fixture programs).

Adopters run evals in CI beside their own code, where company policy and licence scanners expect
a software licence, and Creative Commons does not recommend its licences for software. The first
planned adopters are a corporate team, so the evals, like the skills, should not need a licence
review.

## Options

- **CC BY 4.0, like the skills.** One licence for the repo, but a CC licence on code that CC
  itself advises against.
- **Split by file type:** code under a software licence, prose and data under CC BY. Precise, but
  it asks a reader to check a licence per file. skillboss-dojo chose whole directories with "no
  file-level exceptions, because nobody reads a licence per file"
  ([mazzyst/skillboss-dojo#13](https://github.com/mazzyst/skillboss-dojo/pull/13)).
- **MIT.** Short and permissive, with no patent grant.
- **Apache-2.0.** Permissive, with an express patent grant, and covers any work of authorship, so
  prose and data are as well served as code.

## Decision

Apache-2.0 for everything under `evals/`, prose, data, and code alike, copyright Hampton Maxwell.
`evals/LICENSE` is the verbatim licence text, and the README's License section names the split:
CC BY 4.0 for the rest of the repo, Apache-2.0 for `evals/`.

## Consequences

- Every case lives under `evals/`, whatever its layout (0015, proposed), so one file covers them
  all and no case needs a header of its own.
- Skill text quoted in an eval is thereby also offered under Apache-2.0.
- Third-party material in a case, such as captured output, keeps its own terms; the licence
  covers only what the owner holds. `fixtures` rule 9 already admits only what can be licensed.
- `plugin.json`'s `license` takes an SPDX identifier. Whether it accepts the expression
  `CC-BY-4.0 AND Apache-2.0` is checked in the PR that implements this. Open.
