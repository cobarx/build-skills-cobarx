# Open questions

Unsettled. Moved here out of conversation so it survives.

## This repo

**The five thresholds in `simplicity` are borrowed, not chosen.** Cognitive complexity 15, nesting
depth 3, function 50 lines, file 300 lines, parameters 4. These are common SonarJS and ESLint
defaults. They are plausible and unconfirmed, and presenting them as settled is fake precision.

**Licence undecided.** No `LICENSE` yet.

**Repo is private.** Created private as the reversible default, not as a decision. `ai-skills-cobarx`
stays independently shareable, which was the reason for a separate repo at all.

**`docs/essays/` is a coinage.** There is no strong industry term for a post-hoc narrative about
why a practice exists. Oxide's RFDs are the closest published model but are pre-decision. Recorded
as ours per the vocabulary rule, and open to a better name.

**Decision records do not exist.** Each skill ends with a glob pointing at
`docs/decisions/*-<skill>-*.md`, which currently matches nothing. At minimum these are owed:

- Why the outline is the skill (the essay exists, the record does not)
- Why `linting` owns mechanism and not policy
- Why `definition-of-done` stayed separate from `simplicity`
- Why Brooks's essential/accidental rather than a spend/save/earn coinage
- Why industry terms over our own
- Why the adversarial stance is not a skill
- Why three documentation classes rather than two

**No linting or formatting configured in this repo yet.** A skills repo that preaches lint-from-day-one
and ships without it is its own counterexample. Markdown is the only file type here, so the
question is whether non-code linting counts, which is itself an open question below.

## For `linting`, before it can be written

**How is a linter chosen for a stack?** The missing procedure. Starting position: ask whether the
ecosystem has converged and whether the tool ships with the toolchain, rather than running a
feature comparison. clippy and ruff largely settle their own languages on those two questions
alone.

**Does non-code linting belong in scope?** Markdown, YAML, shell. Real, but arguably a different
concern from code quality gates, and including it starts the scope creep this skill is most
vulnerable to.

**How does lint run locally?** Rule 6 of the draft says local and CI share a config, but not *how*
local runs. Pre-commit hook versus editor integration versus a watch task is a tooling choice, and
naming one felt like policy rather than mechanism.

**Should waivers expire?** MetanoiaFramework's `feature-flags` has review-by dates. The same idea
could stop an inline disable outliving its reason. Probably over-engineering for solo work, but it
is the kind of thing that rots quietly.

## Method

**Does "draft long, then keep only what is a rule" need a home of its own?** It generalises past
skill authoring to specs, docs, and any distillation task. Currently it lives only in
`docs/essays/outline-is-the-skill.md` and in `CLAUDE.md` as a convention.

## Stranded elsewhere

Research for the **playhead** project, including the caption test corpus (Sintel's ~40 languages,
`w3c/imsc-tests` with PNG reference renderings, the real-versus-synthetic fixture split, and the
caution against vendoring OpenSubtitles), currently exists only in the session plan file at
`~/.claude/plans/`. It belongs in `~/code/playhead/docs/` and should be moved there when that
project is next picked up.
