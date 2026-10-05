# What dominates when the how is cheap

Working notes, 2026-10-05. Not settled. Drawn from comparing the skills against the
[chief-of-staff pattern](https://asyncdot.com/blog/chief-of-staff-pattern-orchestrating-claude-code-sessions/)
for orchestrating Claude Code sessions. The article was read through a summarizer, so claims about
it are medium confidence.

## Where we arrived

**The what dominates; the how is an implementation detail, in most pure software systems.**
Hampton's claim. When agents make the how cheap to replace, choosing it stops gating the work, and
product fit (what the output lets its user do) becomes the scarce, valuable part. Engineers miss
this because their sense of what matters was calibrated when a rewrite cost months, so they assume
their choices (DynamoDB vs MySQL) matter. They matter at massive data sets and costs, not by
default.

**You replace the gating choice, not the system.** Moving from AWS to GCP means redoing the infra
layer and the vendor SDK clients, not the app. Industry term: ports and adapters (hexagonal
architecture). The swap is as big as the leak: SDK types that escaped into application code make
the gating choice everywhere.

**That is why these skills insist on separation of concerns and contract enforcement.** Hampton's
point. `contracts` (units meet only at explicit contracts, a supplier wrapped behind one) and
`simplicity` (one unit, concerns as peers) keep each how behind a boundary small enough to replace.
The skills are what make the how disposable, which is what frees attention for the what. The same
boundary pays twice: a component reasoned about in isolation, with only its contract in view, is
the cognitive-load reduction `simplicity` exists for, and it is what lets a human audit agent output
one component at a time.

**Cheap to write is not cheap to verify.** A replacement is safe only when the spec is complete
(`spec` rule 10), the contract holds (`contracts` rules 1 and 2), and checks assert the goal rather
than the implementation (`definition-of-done`, planned `test-fidelity`). Cheap rewrites move the
cost from building to verifying, and the skills sit on the verifying side.

**The how still gates where it holds state or has callers you do not control.** Data (the
migration, not the engine), published contracts, irreversible or regulated actions. Consistent
with `contracts` rule 4: a data shape at a boundary is part of the what.

**The chief-of-staff pattern optimizes the how.** Its loop (re-run claimed commands, read diffs,
make the verifier fail first) checks that the work was done correctly against a validation
contract, never whether the contract is the goal. Its machinery (cmux, a board behind an API)
scales production of the how.

**Build skills is human auditable; that pattern is agent centric.** Its state lives behind a tool
(against `durable-context` rule 4), and its auditor is an agent auditing agents, with the human
receiving reports. Here the human sits at the goal (`spec` 3), the decisions (`decision-log` 3),
and the consumable artifact (`definition-of-done` 5). The two connect: if the what dominates and a
human owns it, the system must be readable by that human. (Interpretation, medium confidence.)

## Open threads

**Should `decision-log` rule 4 scale by reversibility?** "Architecture and tooling choices are
decisions" over-invests in choices a replacement can undo. Industry term: one-way vs two-way
doors. A two-way door may need one line of reasoning, not a framed comparison, the way
`definition-of-done` rule 8 scales proof to blast radius. Not yet checked against the decisions
behind the rule.

**Does `spec` rule 2 underweight prototyping?** If the how is cheap, building several rough
versions and keeping the one that fits may be the main way to find the what, not an occasional
spike.

**The red gate, demoted.** The pattern runs the verifier first and requires it to fail, which
proves the check can fail. We have no equivalent shipped (`tdd` and `test-fidelity` are planned).
Worth having, but subordinate to whether the check is the goal: a red gate on the wrong check
proves only that the wrong check works. Ownership (`definition-of-done`, `tdd`, or
`test-fidelity`) is open.

**Process is not auditable here.** The rules are readable, but whether an agent applied them in a
session is not recorded; the only trail is what `definition-of-done` makes the change show. That
covers outputs, not whether the goal came from its owner. Unclear whether it matters.

**Possible second case for "own the type you accept"** (parked in `planned-skills.md`). Vendor SDK
types leaking into application code is that coupling. It is hypothetical here, not an observed
instance, so it does not yet count toward the rule.
