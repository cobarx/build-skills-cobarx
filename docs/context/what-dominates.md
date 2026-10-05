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
that is easy to delete, not easy to extend" (2016). Not Brooks's "plan to throw one away"
(1975): that is the whole system thrown away once, written before the modularity to rebuild a
subsystem, and Brooks himself later called it too simplistic in favour of incremental building
(1995). Boundaries move disposal from the system to any node, which is the fractal again. Hampton
called it a worse-is-better mindset; in Gabriel's original terms it is closer to the reverse
(worse is better ranks implementation simplicity above the interface), so the label needs care if
used: clean interface, crude disposable internals.

**Accountability is a guiding goal of the project.** Hampton, 2026-10-05: creating accountability
to reverse enshittification was one of the goals for build skills. Not written down anywhere in the
repo before this note. The principle above is its structural form: for every fact, policy,
contract or component, exactly one place answers for it when it is wrong. The rest of the skills
read as accountability too: a reviewer independent of the author (`review` 1), evidence instead of
claims (`definition-of-done` 1), reasoning in the open (`decision-log`), a goal from a named owner
(`spec` 3), rules a human can audit. An agent cannot be held to account, so the accountable role
at the what is a human, which is what the agent-centric chief-of-staff pattern leaves unassigned.
(Interpretation, medium confidence.)

**Accountability is relational.** Hampton: accountable to whom, and to what principles. Enshittification
shows it: the product owner reports to someone who is not the customer, so the chain of answering
points away from the user. Single accountability alone is structure without direction. The skills
already give both relations for the what: to whom is the user (`spec` 5, the goal is what the
output lets its user do; `spec` 3, the person whose problem it is), and to what is the declared
standard (`review` 2, check the declared standard, not one you invent). Two cautions: "owner" in
`spec` 3 means the person whose problem it is, but the word collides with the product owner role,
which is exactly the enshittification chain; and "one place answers for each thing" and "answering
ends at the user, against declared principles" may be two principles, not one (`simplicity` 1).
Scope: the skills can point the engineering chain at the user; they cannot change who the product
owner reports to.

**Two principles: single accountability, and operate in the open.** Hampton, 2026-10-05: two for
sure. The first is structural: exactly one place answers for each thing. The second is direction:
the product owner answers to the agent, and through it to the world. The framework embeds
anti-enshittification principles in everything it does, so an agent using it surfaces what those
principles require and records it in the open; the product owner decides. "If somebody uses these
skills and deliberately ignores the agent, that's on them. They decide." The mechanism already
exists: state it once and proceed if reaffirmed (`simplicity` 7), overriding a default is a logged
decision (`simplicity` 5), a noticed problem is filed without asking (`durable-context` 6), a
blocker is reported rather than routed around (`review` 3). Ignoring the principles stays possible,
but it becomes a visible choice with a name on it. Accountability built this way is bottom up: the
product owner must be accountable, so they must make the manager accountable, so the manager
makes the director accountable. An override at any level is recorded in the open with a name on
it, so it carries upward instead of disappearing. The same shape at every rung, which is the
fractal again, applied to an organization. Analogue: the Toyota andon cord, where anyone surfaces
a problem and it travels up. Limit: the skills make the record exist and stay findable; they
cannot make anyone above read it. "If I can't trust what you do in secret, you're
not particularly trustworthy." The repo practices openness throughout: `durable-context` ("in the
open"), `decision-log` ("a decision is reasoned in the open"), rules a human can audit, a public
repo under CC-BY. Industry term: working in the open (GDS, "make things open: it makes things
better"; Mozilla).

## Open threads

**Where is the project's goal stated?** Accountability to reverse enshittification is a guiding
goal but appears in neither the README nor AGENTS.md (`spec` 4: keep the goal written down where
both can see it). Wording is Hampton's.

**What to call the principle, if not DRY?** DRY is the wrong branding (heard as "don't repeat
code," which the framework permits inside a boundary) but the right genealogy, cited as where the
principle comes from: Codd (data), Hunt and Thomas (knowledge), Parnas (modules). Hampton,
2026-10-05: the principle is single source of truth extended to new domains (contracts, skills,
data models, components). That describes it, but "single source of truth" carries data-centric
baggage, so it needs a different term, recorded as ours if coined. Candidates: single ownership
(matches the "X owns Y" wording already used across the repo; Rust's ownership is a near
namesake), or Raymond's SPOT rule (single point of truth, applied to code as well as data in
*The Art of Unix Programming*; attribution from memory, unchecked). Where it is stated (the
thread above) is also open; the term goes in a decision record when it lands.
Hampton: ownership is a role, not a mentality or culture. Whatever the term, it means an assigned
role, one per thing. The cultural sense ("take ownership," "everyone owns quality") is the
opposite: shared ownership is no owner. Role-based precedents: RACI (exactly one Accountable per
task), Amazon's single-threaded owner.
Hampton: "accountable" is a lot better. The term should build on accountability, not ownership.


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
covers outputs, not whether the goal came from its owner. Under "operate in the open" this matters:
an agent's session is the part done in secret.

**Possible second case for "own the type you accept"** (parked in `planned-skills.md`). Vendor SDK
types leaking into application code is that coupling. It is hypothetical here, not an observed
instance, so it does not yet count toward the rule.
