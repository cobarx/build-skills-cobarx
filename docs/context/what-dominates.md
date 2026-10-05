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
cannot make anyone above read it. Hampton: that is what the decision log does when done
properly. And Toyota in essence makes the line worker a manager of the plant: anyone can
stop the line. The principle is jidoka (stop on an abnormality rather than pass it on); the andon
cord is the signal. The agent using these skills is the line worker: it stops and surfaces
(`review` 3, blocked rather than passed; `durable-context` 6, filed without asking), and the
person accountable decides whether the line restarts. "If I can't trust what you do in secret, you're
not particularly trustworthy." The repo practices openness throughout: `durable-context` ("in the
open"), `decision-log` ("a decision is reasoned in the open"), rules a human can audit, a public
repo under CC-BY. Industry term: working in the open (GDS, "make things open: it makes things
better"; Mozilla).

**Deming and TQM: measure it and make it better.** Hampton, 2026-10-05: one of the spiritual
principles behind the project, forgotten until this conversation and written down nowhere before
this note. Much of the repo already reads as Deming:
- Build quality in rather than inspect it in (point 3): spec before building, the tell built into
  the artifact (`definition-of-done` 6), the planned red gate and `test-fidelity`.
- Bring data, not claims: `definition-of-done` 1, show the measured value beside the expected one.
- Eliminate numerical quotas (point 11): `simplicity`'s thresholds are "diagnostics, not targets";
  `spec` 5, the goal is not a number it hits. Measure to understand, never as the target.
- The system, not the person: most defects are the system's, which management owns. That is the
  bottom-up chain above, each level accountable for the system it runs.
- Drive out fear (point 8): stopping the line has to be safe, or no one pulls the cord.
- Plan, do, study, act: `spec`, build, `definition-of-done`, then supersede in the decision log.
Where "measure it" is thin: the skills themselves are not yet measured. `evals/` holds only its
licence (0019); the `simplicity` thresholds are borrowed, not measured (open questions); whether
skills load deep in a long session is untested (#58).

**This is a TQM framework.** Hampton, 2026-10-05. The other identities sit under it. TQM's usual
principles, mapped:
- Customer focus: `spec` 5, the goal is what the output lets its user do.
- Total involvement: the agent as line worker, able to stop the line.
- Process centered: the skills are process standards, not outcome targets.
- Integrated system: the fractal; the same invariants at every level.
- Continual improvement: supersede, never edit; essay revisions; planned evals.
- Fact-based decisions: `definition-of-done` 1, show the measured value.
- Communication: operate in the open.
Spec driven is customer focus made concrete; single accountability and operating in the open are
its accountability and communication. Genealogy: Deming and TQM, the Toyota Production System,
Lean, then Lean software development (Poppendieck: eliminate waste, build integrity in, decide as
late as possible, empower the team, see the whole). What is new is the line worker being an agent.

**Each unit must be measurable and scorable.** Hampton, 2026-10-05, a principle discussed in
another session today and not found recorded anywhere in the repo or its branches. TQM reinforces
it, and it is part of why single accountability matters: a score needs one unit to attach to. A
score on a fact two units own has no one to answer for it; an owner with no score cannot be held to
account. Scored against the goal (`spec` 5), as a diagnostic, never a quota (Deming's point 11,
`simplicity`'s "diagnostics, not targets"). A unit's score is also what tells you to dispose of it.
The eval drafts already carry the positive controls the chief-of-staff article asks for: a
known-bad case expected to score 0 and a known-good case expected to score 1.0 (draft 0017, #64;
#61).

Hampton: engineers say "I have an OpenAPI contract," 0 or 1; TQM says "I have a score." Both are
kept, answering different questions. The contract stays binary: may this unit plug in? A contract
mostly honoured is broken, and a replacement must conform fully, which is what makes it
disposable. The score sits on top: how well does it serve the goal? Industry form: conformance to
specification (Crosby, zero defects, the goalpost model) versus Taguchi's loss function, where
quality degrades continuously with distance from the target, inside the spec limits as well as
outside. `definition-of-done` 1 leans Taguchi already: the measured value beside the expected one,
not a check mark.

Hampton: the score is like a movie review, one score per dimension (set design, costumes, sound,
special effects, casting, script, each 0 to 10). An analytic rubric, as opposed to a holistic one.
Each dimension has one accountable owner (the film credits are the ownership map: production
designer, costume designer, sound, VFX supervisor, casting director, writer), which is single
accountability and scoring as one system. `definition-of-done` 3 already enumerates every
dimension; this scores each instead of passing it. The whole is scored apart from its parts: a
film can score well on every craft and still not work, which is `definition-of-done` 7 and
`spec` 10, and the director owns that score.

**Closed systems neglect developer experience.** Hampton's observation: engineers writing code
outside open systems routinely do not prioritize DX. A reading through the principles above: an
internal consumer is captive, so nothing holds the author to account for their experience, which
is the enshittification mechanism (lock-in removes accountability to the user) at the scale of a
module. Open source answers to the world and to users who can leave. Under the fractal every unit
has a user, often a developer (or now an agent) calling its contract, so DX is customer focus at
that level, and in the scorecard it is the dimension closed systems leave unscored. It matches
`contracts`: internal boundaries do not announce themselves, which is where coupling accumulates;
they are also where DX goes unmeasured. Where closed organizations do prioritize DX, it is by
adopting the product framing on purpose (platform as a product, Team Topologies).
Hampton: Amazon figured this out too; sell your internal systems. The Bezos API mandate (around
2002, known through Steve Yegge's 2011 post, so secondhand) required every team to expose its data
and functionality only through service interfaces, with no direct linking or reading another
team's data store, and every interface "designed from the ground up to be externalizable." That
is `contracts` (no third source), single accountability (each team owns its data), and DX forced by
treating every internal consumer as a potential external customer. AWS is the case where the
internal systems were in fact sold. (The "excess capacity" origin story is disputed by Amazon;
the mandate is the stronger evidence.)
Hampton: every system had to compete on the market, not just AWS. Examples, sourced 2026-10-05:
- Fulfillment by Amazon (2006): Amazon's warehouses sold to third-party sellers; Buy with Prime
  (2022, open to all US merchants 2023) extends it to merchants' own sites.
- Amazon Supply Chain Services (2026): freight, warehousing, fulfillment and parcel, open to any
  business, not only Amazon sellers (P&G, 3M, Lands' End).
- Mechanical Turk (2005): built to find duplicate product pages in Amazon's catalog, then sold.
- Amazon Connect (2017): the contact center behind Amazon's retail customer service, sold
  through AWS.
- Just Walk Out: pulled from most Amazon Fresh stores, yet in 375+ third-party venues
  (stadiums, airports). The market scored it differently than its home did.
Outside Amazon: Walmart Commerce Technologies (GoLocal delivery, 2021; Route Optimization as SaaS;
Store Assist via Salesforce), and Ocado, a grocer that sells its warehouse platform to 13 partners
including Kroger. The market is the outside scorecard that a captive internal consumer cannot be.
Hampton: backend is a how no one cares about, unless you are Amazon or someone doing massive
logistics. There the backend is either the scale constraint (the earlier exception) or it is sold,
and then it is no longer a how: it has its own users and is scored as a product (FBA, AWS).
Sources: [FBA](https://www.marketplacepulse.com/articles/a-decade-of-fulfillment-by-amazon-fba),
[Buy with Prime](https://www.aboutamazon.com/news/retail/prime-shopping-expands-beyond-amazon-com),
[ASCS](https://www.cnbc.com/2026/05/04/amazon-opens-up-its-logistics-network-to-other-businesses-in-new-growth-push.html),
[MTurk](https://spectrum.ieee.org/untold-history-of-ai-mechanical-turk-revisited-tktkt),
[Connect](https://siliconangle.com/2026/04/28/amazon-connects-second-act-contact-center-agentic-ai-suite/),
[Just Walk Out](https://www.webpronews.com/amazons-just-walk-out-technology-pivots-to-third-party-venues-after-grocery-store-retreat/),
[Walmart](https://chainstoreage.com/walmart-sell-its-ai-logistics-tool-other-businesses),
[Ocado](https://www.digitalcommerce360.com/2025/12/30/kroger-partner-ocado-group-ends-exclusivity-agreements-us-supermarkets/).

## Open threads

**Where is the project's goal stated?** Accountability to reverse enshittification is a guiding
goal but appears in neither the README nor AGENTS.md (`spec` 4: keep the goal written down where
both can see it). Wording is Hampton's.

**Decision records name the recorder, not the decider.** Every record here carries "Decided: date ·
Recorded: date · Claude Opus 5.5", the name of whoever wrote it down. None names who decided. For
the decision log to carry accountability upward, the accountable party has to be on the record.
MADR has an optional `decision-makers` field (0001 adopts MADR). Whether `decision-log` should
require it is open.

**Is TQM the brand or the genealogy?** As with DRY, the term carries baggage: a 1990s corporate
programme, associated with ISO 9000 paperwork and quality circles, largely succeeded by Lean and
Six Sigma. It may be the right lineage and the wrong label, or the right label with its meaning
stated. Hampton's call.

**Building the rubric.** Hampton, 2026-10-05: start building a rubric whose scores measure UI
elegance, product fit, reliability, ease of adoption and long-term maintainability, things rarely
measured in corporate America. Goal not yet written (`spec` 1): what the rubric lets its user do,
who that user is, and which unit is scored first. Open, to ask:
- Which unit first? Answered 2026-10-05: features and products, not backend services. So each
  dimension is as the user meets it: reliability as experienced, not an SLO; adoption as a new
  user's path to value; maintainability of the feature as it evolves.
- What decision do the scores feed (ship, fix, replace, dispose, invest)? That is the rubric's
  goal (`spec` 5), and it sets the scale and who reads it.
- A score can be a number or a verdict in words: "the set design is trash," with its reason, is as
  valid as a 3 out of 10, and usually says more about what to fix. The critic's judgement, not
  only a count.
- Who scores each dimension? Elegance and product fit need use by the person the output is for
  (`definition-of-done` 4); an agent that cannot judge one reports it blocked (`review` 3).
- Who owns each dimension, so every score has one party who answers for it?
- Which dimensions apply at which level of the fractal (product fit at product and feature,
  maintainability at component)?
Prior art to check before inventing (`adopting-standards`), guesses until checked: ISO/IEC 25010
(product quality: reliability, maintainability, usability among its characteristics), Google's
HEART framework (adoption, task success), behaviourally anchored rating scales (each score point
described by an observable example, so a 7 means the same to every scorer). Elegance has no
standard I know of. Risk: hard-to-measure qualities invite proxies (Goodhart), which the scores
must resist by staying diagnostic.

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
