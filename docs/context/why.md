# The why: what build skills is for

Working notes, 2026-10-05. Not settled. From a session comparing the skills against the
[chief-of-staff pattern](https://asyncdot.com/blog/chief-of-staff-pattern-orchestrating-claude-code-sessions/)
for orchestrating Claude Code sessions (Mithushan Jalangan, 2026-09-19), read in full.

Why comes first in the chain why, then what, then how. Companions:
[what-dominates.md](what-dominates.md) (the what over the how) and
[product-rubric.md](product-rubric.md) (scoring what gets built).

## Where we arrived

**Why build anything that's not that good?** Hampton, 2026-10-05, closing the thread. Mediocre work
gets built when accountability points away from the user, when good goes unmeasured, and when
getting the how to work was itself the bar. Replaceable hows (see what-dominates.md) remove the last
excuse. Hampton: and cheap is cutting corners. Inexpensive to replace is not cheap; a replaceable
how is still built well. Already in the skills: `simplicity` 8 (the cheapest change is the one not
written), `definition-of-done` 7 (demo for quality, not only correctness), and
`define-what-good-looks-like` ("more mediocrity traces to a goal never set than to a job done
badly"). The exception is a prototype, deliberately rough to find the what (`spec` 2): fine, so long
as it is kept for its lessons and never shipped as finished. Hampton's answer to his own question:
because you don't know how. The fourth reason, and the deepest: knowing what good looks like, and
how to reach it, takes experience (`define-what-good-looks-like`). Deming's points 6 and 13
(training, education). It is the reason the skills exist: to carry that knowledge, so a little
effort reaches good work (the pit of success). "How" here is craft knowledge of quality, not the
implementation how. Hampton: but take accountability seriously and you have to get the training and
education. Not knowing how is not a root cause beside accountability; accountability drives the
learning. Nietzsche (Twilight of the Idols, 1889, popularized by Frankl): "If we have our own why of
life, we shall get along with almost any how." Give a great enough why and any how can be borne. The
idea is Nietzsche's; Hampton found how it applies here. The order is why, then what, then how; the
planned *why* skill in `planned-skills.md` ("why before what") is the first link.

**The builder's why: fun, useful, pride.** Hampton, 2026-10-05: if I'm building something, I want
fun, I want useful, I want pride in what I've built. Useful is the user's why (`spec` 5); fun and
pride are the builder's. Deming's point 12: remove the barriers that rob people of their right to
pride of workmanship. Note against the planned *why* skill's source ranking, which calls a
lifelong dream the weakest evidence: as evidence that the goal is right it may be, but as fuel it
can be the strongest. The why as evidence sets direction; the why as purpose keeps the work going.

**Accountability is a guiding goal of the project.** Hampton, 2026-10-05: creating accountability
to reverse enshittification was one of the goals for build skills. Not written down anywhere in the
repo before this note. Its structural form is single accountability, below: for every fact, policy,
contract or component, exactly one place answers for it when it is wrong. The rest of the skills
read as accountability too: a reviewer independent of the author (`review` 1), evidence instead of
claims (`definition-of-done` 1), reasoning in the open (`decision-log`), a goal from a named owner
(`spec` 3), rules a human can audit. An agent cannot be held to account, so the accountable role
at the what is a human, which is what the agent-centric chief-of-staff pattern leaves unassigned.
(Interpretation, medium confidence.)

**Accountability is relational.** Hampton: accountable to whom, and to what principles.
Enshittification shows it: the product owner reports to someone who is not the customer, so the
chain of answering points away from the user. Single accountability alone is structure without
direction. The skills already give both relations for the what: to whom is the user (`spec` 5, the
goal is what the output lets its user do; `spec` 3, the person whose problem it is), and to what is
the declared standard (`review` 2, check the declared standard, not one you invent). Two cautions:
"owner" in `spec` 3 means the person whose problem it is, but the word collides with the product
owner role, which is exactly the enshittification chain; and "one place answers for each thing" and
"answering ends at the user, against declared principles" may be two principles, not one
(`simplicity` 1). Scope: the skills can point the engineering chain at the user; they cannot change
who the product owner reports to.

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
product owner must be accountable, so they must make the manager accountable, so the manager makes
the director accountable. An override at any level is recorded in the open with a name on it, so it
carries upward instead of disappearing. The same shape at every rung, which is the fractal again,
applied to an organization. Analogue: the Toyota andon cord, where anyone surfaces a problem and it
travels up. Limit: the skills make the record exist and stay findable; they cannot make anyone above
read it. Hampton: that is what the decision log does when done properly. And Toyota in essence makes
the line worker a manager of the plant: anyone can stop the line. The principle is jidoka (stop on
an abnormality rather than pass it on); the andon cord is the signal. The agent using these skills
is the line worker: it stops and surfaces (`review` 3, blocked rather than passed; `durable-context`
6, filed without asking), and the person accountable decides whether the line restarts. "If I can't
trust what you do in secret, you're not particularly trustworthy." The repo practices openness
throughout: `durable-context` ("in the open"), `decision-log` ("a decision is reasoned in the
open"), rules a human can audit, a public repo under CC-BY. Industry term: working in the open (GDS,
"make things open: it makes things better"; Mozilla).

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

**Disposable is an anti-principle.** Hampton, 2026-10-05, refining his earlier "I want to throw
things away" (kept as said in what-dominates.md). A good product can be repaired, recycled or
repurposed. Good software may not persist, but at the least it leaves useful lessons and is an
evolution towards the next, better iteration. macOS releases were never disposable: Apple built the
Mac one annual release at a time. Boundaries exist so a part can be replaced while the whole
evolves, not so things can be thrown away. That is kaizen, continuous improvement, which puts it
back inside TQM; "disposable" was the opposite. Industry terms: evolutionary architecture (Ford,
Parsons, Kua); repair, reuse, recycle from the circular economy. The lessons persist even when the
code does not, which is what `durable-context` and the essays are for.

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

**A product framework, not a software one.** Hampton, 2026-10-05: build skills is a product
framework that happens to have a lot of software terminology and policy; nothing in it should
presuppose that you are building software. That is the aim. A rough read of the skills against it
(Claude's, medium confidence):
- General, with software examples: `spec`, `definition-of-done`, `review`, `decision-log`,
  `durable-context`, `simplicity` (its thresholds aside), `contracts`, `adopting-standards`,
  `essays`.
- Bound to software as written: `naming` (identifiers), `format`, `fixtures`, `parallel-work`
  (worktrees and branches), `platform-correctness`, `skill-versioning`, and planned `linting`.
That may be the fractal again: general principles, with software as one domain they apply to.
Hampton, revised from use: in practice it is basically a software framework that extends well to
certain aspects of other product domains. The product framework is the aim; the software framework
is what exists. The general skills above are the parts that extend.

## Open threads

**The stated purpose says software.** The README opens "Skills for how software gets built," and
AGENTS.md says the same. Accurate for what exists, silent on the aim. Whether and how to state the
aim is Hampton's call, and his wording.

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

**What to call the principle, if not DRY?** DRY is the wrong branding (heard as "don't repeat
code," which the framework permits inside a boundary) but the right genealogy, cited as where the
principle comes from: Codd (data), Hunt and Thomas (knowledge), Parnas (modules). Hampton,
2026-10-05: the principle is single source of truth extended to new domains (contracts, skills,
data models, components). That describes it, but "single source of truth" carries data-centric
baggage, so it needs a different term, recorded as ours if coined. Candidates: single ownership
(matches the "X owns Y" wording already used across the repo; Rust's ownership is a near
namesake), or Raymond's SPOT rule (single point of truth, applied to code as well as data in
*The Art of Unix Programming*; attribution from memory, unchecked). Where it is stated (the
thread below) is also open; the term goes in a decision record when it lands.
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

**Process is not auditable here.** The rules are readable, but whether an agent applied them in a
session is not recorded; the only trail is what `definition-of-done` makes the change show. That
covers outputs, not whether the goal came from its owner. Under "operate in the open" this matters:
an agent's session is the part done in secret.
