# Planned skills

Designs settled in conversation but not yet written. Working notes, not commitments.

## `linting` — enforce the rules mechanically from the first commit

Owns the **mechanism only**. Holds no policy of its own: every rule it runs is required by another
skill, which owns the threshold and the rationale.

A first draft was rejected for being stances rather than procedures ("errors not warnings" is a
position, not something you can do). Rebuild around two things: a **selection procedure** for
picking the linter for a stack, and this **enforcement table**.

| Principle | Linter enforces | Residue and its owner |
|---|---|---|
| Separation of concerns | `eslint-plugin-boundaries`, `import/no-cycle`, `import/no-internal-modules`, `import/max-dependencies` | Where boundaries belong, `contracts` |
| Simplicity | `sonarjs/cognitive-complexity`, `complexity`, `max-depth`, `max-lines`, `max-lines-per-function`, `max-params`, `max-statements`, `no-unused-vars` | Whether a unit of work is one thing, `simplicity` rule 1 |
| Documentation presence | `jsdoc/require-jsdoc`, `require-param`, `require-returns`, `check-param-names`; Rust `#![warn(missing_docs)]` | Whether the doc says anything, `contracts` |
| Legibility | `id-denylist`, `id-length`, `no-shadow`, `unicorn/prevent-abbreviations` | Whether a name is accurate, `naming` |
| One thing, named for it | `naming-convention` custom regex for approved verb prefixes; `max-statements` as a weak proxy | Whether the name is true of the body, `naming` |

Scope the documentation requirement to the **exported surface only**. Mandatory JSDoc everywhere
manufactures `/** Gets the name. */ getName()`. On a public API the doc is part of the contract;
internally the name carries it.

Verified rather than recalled: [`naming-convention`](https://typescript-eslint.io/rules/naming-convention/)
takes `custom: { regex, match }`, and [`id-denylist`](https://eslint.org/docs/latest/rules/id-denylist)
exists for exactly this purpose.

Four written skills already contain promises `linting` has to keep, so those references dangle
until it exists.

## `test-fidelity` — a test must be able to fail for the real reason

Fully designed, zero remaining design work. Five rules, each a way a test loses that ability:

1. **Place the test at the seam.** A test far from the failure fails for a proxy reason. Unit
   tests where the logic is; contract tests at every service boundary, including local utilities
   and shell scripts, which is the part people skip.
2. **Cover every dimension.** Unit, integration, e2e, browser. A missing kind means that class of
   failure cannot be caught at all. Presence across kinds, not the test pyramid's proportions.
3. **Test in an environment that tells the truth.** Where deployed differs from local, test where
   it deploys. A fake environment produces fake passes.
4. **Use real data, never invented mocks.** A mock makes the test pass for a reason real data
   would not. Establish a corpus and use it.
5. **Write the test that tries to break it.** Boundary, empty, malformed, out of order,
   concurrent, hostile. A suite with no failing-input tests is confirmation bias with a green
   checkmark.

Named `test-fidelity` because plain `testing` admits anything, failing `naming` rule 2.

Splits: `fixtures` owns the corpus mechanism (capture, organise, grow), this owns the rule. `tdd`
owns test-first timing, this owns test design. They are counterparts, since tdd's "watch it fail
for the right reason" is this rule at runtime.

## `contracts` — units meet only at explicit contracts, never internals

From wheelviser. Three parts worth keeping verbatim:

- **Two sources.** The API gives shape, the spec gives behaviour. `contracts` and `spec` are a
  pair, which is why writing one without the other leaves half a contract.
- **Completeness is falsifiable.** A gap you cannot fill from them means the contract is
  incomplete. You never argue about it; you try to build a client and find out.
- **The remedy is directional.** Extend the contract first, same PR. Never reach inside.

**The checkpoint**, because a linter enforces the *import* boundary but not the *reading*
boundary:

> Work from the spec and public API only. If you open the implementation to answer a question,
> that question *is* the contract gap. Record it, extend the contract, continue. Do not answer it
> by reading.

Testable in review by asking what you had to open. This matters more for AI-assisted work than
human work, since nothing but the discipline stops an agent reading any file.

## `definition-of-done` — establish when a unit is complete

Spine is **burden of proof**: the change justifies itself, and silence is not approval. That is a
stronger shape than a checklist of boxes.

Kept separate from `simplicity` because it cuts across `spec`, `contracts`, `linting` and
`decision-log`, and a cross-cutting concern belongs beside the things it cuts across rather than
inside one of them (`simplicity` rule 2).

## `spec` — define what the system must do before choosing how

Owns the **glossary**, and the vocabulary chain: **industry to spec to code**. The spec does not
originate terms, it adopts the established industry term and records the choice; `naming` rule 6
then binds code to what the spec registered.

Domain concepts must use the industry term. Architectural constructs local to a codebase may be
coined, but coinage is recorded in the glossary and marked as ours.

Each glossary entry cites its source, per `platform-correctness` rule 1.

## Also planned

`fixtures` (corpus mechanism), `harness` (make the system locally observable without external
services), `decision-log` (port), `tdd` (port), `error-taxonomy` (port).

## The adversarial stance is not a skill

It has no procedure of its own, and making it one would repeat the rejected `linting` draft. It
lands in three places instead:

- `test-fidelity` rule 5.
- **The shape of every checkpoint.** `naming` predicts before reading; `contracts` asks what you
  had to open. Both set up a falsification with a named disproof condition rather than an
  inspection. **Rule for future checkpoints: phrase as an attempt to disprove, never as a review.**
- `definition-of-done`'s burden of proof.

**The caveat that makes it survivable:** scale to blast radius. A rename needs no defence; a change
to core logic does. Unbounded "prove it" is paralysis, and a rule that fires on everything gets
switched off.

**Specific to solo work:** self-review has a hard ceiling, and that ceiling is the main quality
risk. The adversary role is the one an AI can fill and a person cannot fill for themselves. Make
it an explicitly invoked mode rather than hoping it happens. Two passes, not one: at design, from
the spec and plan, asking what would make this the wrong thing to build; and after implementation,
from the diff, running the checkpoints. The implementation pass runs *before* the author's own
review, or it anchors on the author's framing instead of attacking it.
