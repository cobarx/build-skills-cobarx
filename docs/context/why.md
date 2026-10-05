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
as it is kept for its lessons and never shipped as finished. Hampton's answer to the question:
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

**"So that" is the test of a why.** Hampton, 2026-10-05: all marketing is "so that." I get a job so
that I can get money to spend on the things I want; I get a partner so that I have someone to share
my life with. Ask "so that" of any what and you get its why; ask again until the answer is held for
its own sake. Industry forms: means-end chains and laddering in marketing research (Gutman, 1982;
Reynolds and Gutman, 1988: attribute, then consequence, then value); the user story's "so that"
(Connextra, 2001); Toyota's five whys, which puts it back inside TQM; Rokeach's instrumental versus
terminal values for where the ladder stops.

**The corollary: what else would I rather be spending my time on?** Hampton. Opportunity cost as a
test of the why: a why is great enough only if the work beats the alternatives for the same time.
In the elevated sense, what gives my life purpose. The top of the "so that" ladder is a purpose,
and that is the why great enough to bear any how. For a product it applies twice: the user's time
(is this worth their hour?) and the builder's (fun, useful, pride, above).

**Worth doing well, judged by its why.** "Anything worth doing is worth doing right" is widely
attributed to Hunter S. Thompson, but no primary source was found (2026-10-05). The origin is Lord
Chesterfield, letter to his son, 10 March 1746, published in *Letters to His Son* (1774): "Whatever
is worth doing at all, is worth doing well." Chesterton's rebuttal, *What's Wrong with the World*
(1910), Part 4, Chapter 14: "If a thing is worth doing, it is worth doing badly," meaning the
central things of a life (a love letter, raising children) should be done by amateurs, out of love,
rather than handed to professionals. Hampton: Chesterton is speaking of a life lived by the heart,
and that is doing well. The two agree once "well" is judged against the why rather than the
polish: a love letter is good if the love comes through (`spec` 5, the goal is what the output
lets its user do). Amateur comes from the Latin *amator*, lover.

**Harmless is an incredibly hard goal.** Hampton, 2026-10-05, on Claude's "helpful, honest,
harmless." It is an absence goal, and a negative cannot be proven: a system that does nothing also
reports no harm. It is zero defects (Crosby's goalpost) where real harm is continuous (Taguchi).
Refusal is not harmless either; unhelpfulness has costs, and read literally the goal drives toward
doing nothing. It is relational: harmless to whom? And it is a constraint, not a what (`spec` 5).
Hampton: there are few harmless actions at a social level; almost every action shifts a cost onto
someone. So the standard cannot be harmless. It is harms named, measured continuously, owned, and
recorded in the open, with a human accountable at the point of irreversibility (the andon cord).
Anthropic's own framing has reportedly moved from harmless as an absolute toward weighing harm
against benefit (from memory; the published constitution is the source to check).

**The vendor-promise model didn't work; the law is assigning accountability.** Hampton: there are
now legal proposals, some adopted, that make people accountable for what the agent ships. From
memory, medium-high confidence: Moffatt v. Air Canada (2024) held the airline liable for its
chatbot's answers and rejected the claim that the chatbot answered for itself; the EU's revised
Product Liability Directive (2024) brings software, AI included, under strict product liability;
the EU AI Act puts obligations on deployers as well as builders, phasing in through 2027; US states
including Colorado and California have their own measures. Each assigns a human or a company to
answer for the agent, which is single accountability imposed from outside. Consequences for the
open threads below: the decider on a decision record becomes evidence, an unauditable agent
session becomes a liability exposure, and an artifact the person exercised (`definition-of-done`
1) is a defensible record where "the agent said tests pass" is not.

**Society is an ecosystem; there is no central decider.** Hampton, 2026-10-05. This is the limit
of single accountability: it holds within a node (a team, a product, a company), not at the top.
Society coordinates through overlapping feedback loops: markets, courts, regulators, the press,
norms, users who leave. Ostrom's polycentric governance (many centres of decision, none supreme,
each accountable to the others); Hayek's knowledge problem (no central decider could hold what the
ecosystem knows). So "the product owner answers to the world" means an ecosystem of judges, not a
judge at the top, and the legal turn is one loop tightening. Operating in the open matters more
here: the open record is the interface between nodes that share no boss, and a decision made in
secret escapes every loop. The fractal with its top rung changed: within each node one accountable
owner, between nodes explicit contracts (laws, standards, protocols), above that no owner, as on
the internet. The framework should not claim a root owner it cannot have; it can make every node
accountable and every decision visible, so the loops have something to act on. (Interpretation,
medium confidence.)

**Harmless means different things to different people.** Hampton, 2026-10-05: within a society
there are multiple competing, sometimes mutually exclusive value systems. Isaiah Berlin's value
pluralism: values can be incommensurable, and their conflict is not a mistake to be resolved. So
no definition of harm is neutral; a system that claims to be harmless has silently adopted one
value system and imposes it on people who hold others. The honest move is to declare the values
(operate in the open; `review` 2, check the declared standard), so others can see them, disagree,
and choose. In an ecosystem, pluralism is handled by exit and voice (Hirschman, *Exit, Voice, and
Loyalty*, 1970): people move to products whose values they share, or argue for change. Lock-in
removes exit, which is why it is a harm under nearly every value system: it stops people acting on
their own. (Interpretation, medium confidence.)
Hampton: harmless is a totalizing value, with enormous costs attached. Applied to everything, one
value overrides all the others: refusals, paternalism, one group's values imposed on all, power
concentrated in whoever defines harm. Berlin's warning against value monism (*Two Concepts of
Liberty*, 1958): the belief that all values fit one harmonious whole has been used to justify
coercion. A limit for this framework: single source of truth applies to facts, ownership and
contracts, never to values. One owner per fact; many value systems, declared and in the open.
Hampton: this is an opinionated framework with a clear set of values. Opinionated is not
totalizing: the values are declared, adoption is a choice, and exit stays open. The skills load
one at a time where they apply, the text is CC BY so anyone can fork or adapt it, and a person who
ignores the agent decides that for themselves. Apple's "one way that works" is opinionated in the
same sense; Rails' "opinionated software" is the industry term. The six values, confirmed by
Hampton 2026-10-05:
accountability, operating in the open, quality measured and improved (TQM), the what over the
how, the user's outcome, pride in the work. The gap: an opinionated framework has to state its
opinions, and these are stated nowhere a newcomer reads (the open thread below).

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

**Why corporations stayed antithetical to Deming.** Hampton asked, 2026-10-05: TQM was widely
adopted, so why are corporate structures so largely against what Deming recommended? Claude's
reading, medium confidence: companies adopted the tools and not the philosophy (NUMMI: GM copied the
tools, not the culture), and the tools fit inside the existing structure while the philosophy would
have replaced it. Deming's "seven deadly diseases" read as a description of standard practice: lack
of constancy of purpose, emphasis on short-term profits, annual performance review, mobility of
management, management by visible figures alone. Shareholder-value incentives (agency theory, stock
options, quarterly earnings) point accountability at investors, not customers, the enshittification
chain. Deming put most defects on the system, which management owns; ranking and firing workers
(GE's stack ranking under Welch, beside its Six Sigma) is the easier story. The divisional,
finance-controlled structure (Sloan's GM) measures what is countable. And it is hard: it needs
leaders with deep knowledge and long horizons, the same reason Apple's functional organization is
rarely copied. Hampton: that is where I would like to see the economy move, back to small businesses
with more direct relationships with their customers. A direct relationship is the shortest
accountability chain: the person who decides answers to the customer, with no product owner
reporting to someone else. Agents with these skills extend the startup advantage, so a small team
can integrate concerns and reach quality once reserved for large ones. Counterforces (Claude's
reading): the platforms between small businesses and their customers (app stores, marketplaces, ad
networks) are where Doctorow locates enshittification, so the relationship is direct only if it does
not run through one; compliance costs and scale economies still favour the large. Prior art:
Schumacher, *Small Is Beautiful* (1973). Whether this belongs in the project's stated why is
Hampton's call. Exit and voice are Hirschman's (*Exit, Voice, and Loyalty*, 1970): leave, or speak
up. Hampton: that is also Stallman's goal, freedom as the ability to leave, and to voice when all
else fails by creating your own solution. The four freedoms (run, study and change, redistribute,
distribute changes) make exit and voice structural. A fork is exit that keeps the product, and voice
made concrete: you leave, take it with you, and publish the alternative. Stallman's origin story is
a denied voice: a printer at the MIT AI Lab (around 1980) whose driver source was withheld, so
nobody at the lab could fix it. A live consequence for this repo: copyleft is how Stallman protects
those freedoms downstream. 0014 chose CC BY, which lets an adapter close what they add; CC BY-SA
(copyleft) would not. The reading guide on the open `context/by-vs-by-sa` branch weighs exactly
that. Hampton: it's not an easy choice, and at the end of the day culture still matters: LLVM is
permissive (BSD-style, now Apache 2.0 with LLVM exceptions), Linux is GPL, and both are vibrant.
What sustains both is a culture of contributing upstream, and the economics behind it: carrying a
private fork costs more than upstreaming, whatever the licence allows. Hampton: it's easy to bypass
a licence, but to get the most out of TQM you have to dedicate yourself to the process. Compliance
can be faked; commitment cannot. It is the NUMMI lesson again (the tools copied, the culture not)
and Deming's first point, constancy of purpose. For this repo: a team can load every skill and tick
every box without the commitment, and get little. What produces the commitment is the why, which is
why the why is load bearing and why the essays carry the reasoning beside the rules. Hampton:
they're managing outcomes, managing defects, instead of looking at the system. Deming's distinction,
after Shewhart: common-cause variation comes from the system, special-cause from an identifiable
event, and most variation is common cause. Treating a common-cause defect as special (blaming the
person, reacting to each defect) is what Deming called tampering, and it makes the system worse
(Deming's funnel experiment). Measuring outcomes is still right as feedback on the system; managing
people by them is the failure. The repo already works this way: when an agent missed `spec` in a
session, the fix was to the skill's trigger (0020), not only to that session's output.

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
require it is open. With people now legally accountable for what agents ship, the decider on the
record is evidence, not tidiness.

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
an agent's session is the part done in secret, and under the new liability rules a part someone may
have to answer for.
