# Spec form: what MetanoiaFramework and pubnet-tools teach

**Working notes for decision 0022 (proposed).** What a spec should look like, drawn from one skill
that defined a form and one project that used it for a month. Not settled until the trial below
has run.

Sources, read 2026-09-24:

- **MetanoiaFramework `spec`**: 777-line skill, a template (`templates/spec.md`, version 1.0.0),
  and the decision that adopted Given/When/Then as an experiment (2026-08-17). Written for an author
  with no engineering background whose intent an agent or contractor will build.
- **pubnet-tools `docs/specs/`**: nine specs on Metanoia's template, 2026-08-24 to 2026-09-24;
  67 test citations (`// spec: <slug>#S<n>`), 4 to 11 per spec.
- **build-skills `spec`** before this change: 47 lines on what to specify and how deeply (67 after
  #57). No form.

## Lineage

Almost everything pubnet-tools' specs do is Metanoia's template applied faithfully: stable IDs,
the mandatory failure scenario, Not in scope, Terms, Open questions, Done when, Why. pubnet-tools'
contribution is **evidence of use**, plus a few extensions. An earlier reading credited pubnet-tools
with the form itself; it came from Metanoia.

## Element by element

| Element (Metanoia) | Evidence in pubnet-tools | Proposal |
|---|---|---|
| Given/When/Then, one When | All nine specs | Rule 2 |
| Then is an outcome, not a mechanism; no implementation nouns | The specs carried unchanged through a TypeScript-to-Rust rewrite and onto Android. The strongest evidence the rule works: a spec that named modules would not have survived | Rule 2 |
| Mandatory failure or edge scenario | 9 of 9 have an edge scenario, 7 of 9 a failure | Rule 3 |
| Failure Then says what did not happen | Rarely needed, since the checks write little state; reliability S4 says no ping is attempted | Rule 3 |
| Stable IDs `<slug>#S<n>`, never reused | Every spec cited by tests; dns-leak S5 added later without renumbering | Rule 4 |
| Read existing specs first; no rivals | No duplicates across nine | Rule 1 |
| Never invent a number; open question instead | Open questions carry `Blocks: ticket 004` | Rule 5 |
| Specs updated in place | dns-leak S5, added after a live dual-stack run broke the /24 comparison, with a decision record | Rule 6 |
| Not in scope | 9 of 9 | Template |
| Terms, only where needed | 9 of 9; "Agree" in dns-leak is the case that would have been built wrong | Template; moves to `glossary` when it exists |
| Done when: one line per scenario plus cross-cutting | 8 of 9 have one; **0 boxes ticked in any spec**. The per-scenario lines restate the scenarios; the useful lines are the invariants ("Quad9 never appears") | Rule 7: invariants and cross-cutting bars only |
| Status draft, agreed, implemented, superseded | Only `draft` and `agreed` ever used. An abandoned epic's spec is still `draft` | `implemented` dropped (test citations show it); `abandoned` added |
| `template_version` | 1.0.0 in all nine, never read | Dropped: one library version covers the template (`skill-versioning` rule 3) |
| `owner` | Always the same person | Kept; it matters on a team |
| `related:` | Mixes slugs and paths | Template says repo-relative paths |
| Why this behaviour, two sentences and a link | 8 of 9; reliability's names "the load-bearing distinction this spec exists to settle" | Template |

## What pubnet-tools added

- **A Shape section when the contract is data.** `pubnetdiag-scan` needed an exit-code table and
  `android-host-snapshot` a field shape; Given/When/Then fit neither. Metanoia allows "the interface
  is the requirement" inside a scenario, but a table is clearer. In rule 2 and the template.
- **Resolved questions**, kept with the answer and a dated spike (one spec). Stops a settled question
  being re-asked. In rule 5 and the template, with a boundary: a question that chose between
  options is a decision record.
- **Scenarios grounded in observed cases**: the WPA3 driver failure behind wifi-auth, the bus
  outages behind a draft monitoring spec. Optional line in the template. A candidate for the planned
  *why* skill rather than a `spec-form` rule.

## Left out of Metanoia, and why

- **Eliciting a spec from a non-engineer** (draft first, at most three questions, ask for corrections
  not approval) and the **contract-drafting analogy**. Written for Metanoia's audience. Valuable; a
  candidate for `references/` if the trial shows agents writing specs without asking.
- **Inflection-point call-outs** (say when a spec saved a guess). Unproven in Metanoia by its own
  account, and not a rule about the spec.
- **The worth-speccing questions.** `spec` rules 8 and 9 already set depth; the questions could
  become a reference.
- **The spec-set sweep.** Keys on `implemented` and ticked boxes, neither of which survived use.
- **Never write a sensitive value into a spec.** True of every committed file; belongs with whatever
  governs personal data, not here.
- **The scenario-to-test mapping** (Given = Arrange, When = Act, Then = Assert). `tdd`'s, when ported.

## Standards

Searched per `adopting-standards`: Gherkin, EARS (used by Kiro), GitHub Spec Kit, ISO/IEC/IEEE
29148. Gherkin's steps adopted in part; see 0022 for the weighing.

## The trial

Before 0022 is accepted:

- [ ] **A behaviour spec.** Write the pubnet-tools outage-cause spec (drafted 2026-09-24 on the old
      template) with this skill loaded, and note where a rule was missing, wrong, or ignored.
- [ ] **A data-shape spec**, where Given/When/Then fits badly. Does the Shape rule hold?
- [ ] **An amendment**: change an existing scenario's Then. Did rule 4's citation search happen?
- [ ] **A quiet case**: a one-line unconditional change. The skill should not produce a spec.
- [ ] **An eval** in the `evals/` format (#47's lesson: efficacy, not firing): the same request with
      and without the skill, graded on failure scenarios, invented numbers, and mechanisms in Thens.

Open for the trial:

- Is dropping the per-scenario Done when lines right, or did pubnet-tools just never tick boxes?
  One project and one author is thin evidence.
- `spec-form` is 48 lines, split from `spec` (2026-10-05) so neither passes seventy. A missing rule
  goes in `spec-form`; if it reaches seventy, something extracts to `references/` first.
- **Does the form fit a product that is not software?** Raised 2026-10-05 by the owner: "one
  concern i have is whether the gherkin style spec works for products that are not software, such
  as a physical hardware product like my cat boxes." Asked whether Shape should become a general
  property table with a physical-product trial: "don't know yet, that's something to revisit
  later." What is known so far:
  - Use and test procedures fit: a cat on the lid, a spill wiped up, flat-pack assembly each have a
    precondition, one event and a checkable outcome.
  - Properties fit badly: dimensions, materials, load ratings and compliance have no triggering
    event, and forcing one turns the measurement into the When. Shape (rule 2) is the nearest
    form, but it is written for data.
  - Systems engineering states such requirements as "shall" statements, each verified by test,
    analysis, inspection or demonstration (NASA Systems Engineering Handbook, [5.3 Product
    Verification](https://www.nasa.gov/reference/5-3-product-verification/)).
    Given/When/Then covers test and demonstration only.
  - EARS, set aside in 0022 as "a requirement list, not scenarios with state", was developed at
    Rolls-Royce for a jet engine control system and is used by Dyson; its unconditional pattern
    ("The <system> shall <response>") states a property. A physical product may want it beside the
    scenarios, which would reopen 0022's weighing.
