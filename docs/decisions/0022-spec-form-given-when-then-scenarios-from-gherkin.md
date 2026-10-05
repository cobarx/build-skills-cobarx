# 0022. `spec-form`: Given/When/Then scenarios, adopted in part from Gherkin

- **Status:** Proposed. On trial before acceptance; see
  [docs/context/spec-form-analysis.md](../context/spec-form-analysis.md).
- **Decided:** not yet · **Recorded:** 2026-09-24, revised 2026-10-05 · Claude Opus 5.5
- **Affects:** `spec-form` (new: seven rules and the template), `spec` (a pointer only)

## Context

`spec` said what to specify and how deeply, but not what a spec looks like. Two sources already
answer that. MetanoiaFramework's `spec` (777 lines, with a template) adopted Given/When/Then as an
experiment. pubnet-tools has used that template for a month: nine specs, every one cited by tests
(67 citations), carried unchanged through a TypeScript-to-Rust rewrite and onto Android. Nothing in
this library said to follow either, so a spec's form was invented per project.

## Options

Searched, per `adopting-standards` rule 1:

- **Gherkin** ([reference](https://cucumber.io/docs/gherkin/reference/)): Given/When/Then/And/But
  steps in scenarios, plus Feature, Rule, Background, Scenario Outline, Examples, tags, and step
  definitions that make it executable. The form the BDD ecosystem converged on.
- **EARS** ([Easy Approach to Requirements Syntax](https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax)):
  requirement templates such as "When <trigger>, the <system> shall <response>". Used by
  [Kiro](https://kiro.dev/docs/specs/feature-specs/requirements-first/). A requirement list, not
  scenarios with state.
- **GitHub Spec Kit** ([template](https://github.com/github/spec-kit/blob/main/templates/spec-template.md)):
  user stories with Given/When/Then acceptance scenarios, `FR-###` requirements in MUST language,
  `SC-###` success criteria, inline `[NEEDS CLARIFICATION]` markers. Young and tied to its tooling.
- **ISO/IEC/IEEE 29148**: the formal requirements-specification standard. Far heavier than a unit
  of work needs.
- **Keep `spec` form-free.** Each repo invents its own, and nothing is shared between projects.

## Decision

Adopt Gherkin's scenario steps (Given, When, Then, And) in Markdown, with scenario IDs, as
MetanoiaFramework does. **Taken:** the step keywords and one scenario per behaviour. **Left:**
Feature, Rule, Background, Scenario Outline, Examples, tags, and executable step definitions; a
spec is read, not run. Spec Kit and Metanoia converge on the same step form, which settles it
(`adopting-standards` rule 4).

The form is a peer skill, `spec-form`, not a section of `spec`. Drafted first as `spec` rules 7
to 13, it was split out (2026-10-05) when `spec` had grown to 67 lines under 0020, which put the
merged skill near ninety lines against 0009's seventy. The split also passes the one-sentence test
that the merged skill strained: `spec` governs what to say and how deeply, for any product, and
`spec-form` governs how it is written down. A repo with its own spec form keeps it and logs that
choice.

Where pubnet-tools' use contradicts Metanoia, the proposal follows the use and says so in the
analysis: Done when drops the per-scenario checklist, `implemented` and `template_version` go,
`abandoned` and a Shape section come in.

## Consequences

- `spec` gains only a "Not here" pointer and stays at 67 lines; `spec-form` is 48.
- Whether the form fits products that are not software (a physical product) is open; see the
  analysis.
- Accepting this record waits on the trial in the analysis. If the trial rejects a rule, it is cut
  here before acceptance rather than superseded after.
- Adding a skill is a minor bump.
