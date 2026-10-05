# What dominates when the how is cheap

Working notes, 2026-10-05. Not settled. Drawn from comparing the skills against the
[chief-of-staff pattern](https://asyncdot.com/blog/chief-of-staff-pattern-orchestrating-claude-code-sessions/)
for orchestrating Claude Code sessions (Mithushan Jalangan, 2026-09-19), read in full.

## Where we arrived

**The what dominates; the how is an implementation detail, in most pure software systems.**
Hampton's claim. When agents make the how cheap to replace, choosing it stops gating the work, and
product fit (what the output lets its user do) becomes the scarce, valuable part. Engineers miss
this because their sense of what matters was calibrated when a rewrite cost months, so they assume
their choices (DynamoDB vs MySQL) matter. They matter at massive data sets and costs, not by
default.

**You replace the gating choice, not the system.** Moving from AWS to GCP means redoing the infra
layer and the vendor SDK clients, not the app. Industry terms: ports and adapters (hexagonal
architecture), and for persistence the repository pattern, which is what makes DynamoDB vs MySQL
a swap. A repository isolates the engine only if its interface is shaped by what the domain asks,
not by what the store can query; methods shaped around one store's access patterns carry it
through. Data already in the store still needs a migration either way. The swap is as big as the
leak: SDK types that escaped into application code make the gating choice everywhere.

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
(against `durable-context` rule 4), and its auditor is an agent auditing agents. The human leaves
direction in board comments and receives reports, and a checkpoint is explicitly "not a permission
request". Here the human sits at the goal (`spec` 3), the decisions (`decision-log` 3),
and the consumable artifact (`definition-of-done` 5). The two connect: if the what dominates and a
human owns it, the system must be readable by that human. (Interpretation, medium confidence.)

**A framework you adopt whole vs standards that load where they apply.** Hampton's point. The
pattern only works whole, by its own statement ("without a durable store you are not running this
pattern"), and its parts presuppose each other: the red gate needs a validation contract on a
board card, PROVE needs a delegate. Its standards live in one contract file. So you internalize the
whole framework to use any of it, and it does not carry into a related but separate workflow. Its
general rules ("prove a positive before believing a negative", positive controls for absence
checks, state the denominator) are buried inside it. These skills trigger on events in whatever
workflow is running (0020), so one can be taken into a solo session, a human team, or that loop.
The skills apply to themselves the separation of concerns they demand of code.

**The skills are fractal.** Hampton's observation. Zoom to any level (project, feature, component)
and it is clear on its own. The invariants that repeat: a one-sentence purpose (`simplicity`), a
goal serving its parent's and traced to an owner (`spec` 4, `definition-of-done` 2), a contract at
its edge (`contracts`, "inside a system as much as at its edges"), and the goal shown met. The test
is the `contracts` checkpoint generalized: a level is clear when its questions are answerable
without zooming in. The how at one level is the what at the level below, so "the how is an
implementation detail" holds at every level while each contract holds. The chief-of-staff pattern
cannot be zoomed; it is taken whole.

**Separation of concerns forces normalization.** Hampton's point, from early experience: many
problems are avoided by normalizing data. Drawing a boundary forces the question of which side owns
a fact. What it forces is one owner and one source of truth, not one stored copy: caches, read
models and per-service copies are fine when derived from the owner and known to be copies. A
denormalized store is fine behind a repository; a denormalized interface leaks it (the DynamoDB
single-table case). DRY, as Hunt and Thomas defined it, is the same principle for knowledge:
"every piece of knowledge must have a single, unambiguous, authoritative representation."

**Only one thing owns a thing.** Named here as a key principle. The repo practices it at every
level without stating it: every skill's "Not here" section, every split in `planned-skills.md`
("X owns Y, this owns Z"), "do not give a skill policy that belongs to another" (AGENTS.md, 0003),
one home per kind (`durable-context` 5), references in one direction (skills never link to
context), one registered term per concept (planned `glossary`), decisions superseded rather than
edited. Industry names each cover a slice: single source of truth (data, config), DRY
(knowledge), single responsibility (modules). None covers every level.

**Spec driven and DRY.** Hampton's framing: the skills are a DRY framework as well as a spec-driven
one. The two connect. Spec driven says the what is the authority; DRY says every authority is
singular. The spec is the one authoritative representation of the goal, with one owner (`spec` 3),
and checks and decision criteria derive from it (`spec` 7). `contracts` rule 1 ("two sources, and
no third") is DRY stated directly. Neither identity appears in the README, which says only "skills
for how software gets built."

**DRY about ownership, permissive about code.** Hampton's point: Sandi Metz's "duplication is far
cheaper than the wrong abstraction" is weighted for a code-centric world. Duplicated code inside a
disposable unit is cheap; duplicated infrastructure (two auth systems, two queues, two stores of
the same customer) is a fact with two owners, which enterprise tech rightly forbids. Metz is right
about code and silent on knowledge, so she and DRY-as-defined do not conflict. The boundary is
what makes disposal possible: "I want to throw things away, so I need boundaries to be able to
dispose of them." Prior art: Parnas (decompose by what is likely to change), tef's "write code
that is easy to delete, not easy to extend" (2016), Brooks's "plan to throw one away." Hampton
called it a worse-is-better mindset; in Gabriel's original terms it is closer to the reverse
(worse is better ranks implementation simplicity above the interface), so the label needs care if
used: clean interface, crude disposable internals.

## Open threads

**Does "DRY" carry the wrong reading?** It is popularly heard as "don't repeat code," which drives
premature abstraction. The name may need the original definition quoted beside it, or a term
without the baggage (single source of truth). Partly answered by the next point.

**Where does "only one thing owns a thing" live, and under what name?** It is cross-cutting (it
shows in `simplicity`, `contracts`, `durable-context`, `decision-log` and AGENTS.md), so by
`simplicity` rule 2 it is their peer, not part of one. Whether it is a skill (does it have a
procedure?), a stated principle in AGENTS.md and the README, or an essay is open. So is the name:
an industry term, if one covers every level, or a recorded coinage.

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
