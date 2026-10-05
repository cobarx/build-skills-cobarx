# 0022. `simplicity`'s thresholds move to a reference

- **Status:** Accepted
- **Decided:** 2026-10-05 (#96) · **Recorded:** 2026-10-05 · Claude Opus 5.5
- **Affects:** `simplicity`

## Context

`simplicity` stood at 69 lines against 0009's seventy. #96 adds a rule of three lines, and
`simplicity` is the skill most likely to keep gaining rules: it fires on every unit.

## Options

- **Raise the cap.** Rejected: 0009 says a skill that outgrows it extracts first, and so does
  `simplicity` itself (*Extract, do not raise the threshold*).
- **Squeeze the rule in.** A one-line rule, its case in a footnote, rule 8's two paragraphs joined:
  exactly seventy. Rejected: it loses the rule's reasoning and leaves no room for the next change.
- **Move the thresholds to `references/thresholds.md`.** The thresholds measure code, but
  `simplicity` loads for every unit, including ones with no code: a PR description, a reply.

## Decision

Move them. The table and its diagnostics paragraph go to
[skills/simplicity/references/thresholds.md](../../skills/simplicity/references/thresholds.md),
loaded when writing or reviewing code. Brooks's line (0005) stays in the skill, because it applies
to every unit.

## Consequences

- `simplicity` drops to 58 lines, with room for #96.
- This is the repo's first `references/` file. Installs copy each skill's folder whole, so it ships
  with the skill.
- An agent writing code loads one more file; an agent writing prose loads eleven fewer lines.
