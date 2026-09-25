# Planned skills

**Scratchpad.** In-progress designs for skills not yet written. Messy on purpose, and not
subject to `simplicity` rule 8, which targets output presented as finished.

## Not ready: owning the type you accept

Candidate rule for `contracts`, parked because the first attempt at stating it was too absolute.

The observation: a renderer that accepts `VTTCue` is bound to the browser's cue source even though
it imported nothing illegal. You can honour every import boundary and still be coupled, because
you took their type. It stays invisible until a second source arrives, which is why the second
source is always the expensive one.

The correction that stopped it becoming a rule: modelling on a well-designed existing type is a
good starting point, especially in an unfamiliar domain where you do not yet know what your inputs
look like. Defaulting to it is the failure; using it as a reference is not.

Probable shape: **own the type, whatever shape it borrows.** Borrowing a design is fine; accepting
the supplier's type is the coupling, because you cannot change it.

One instance, one correction. Needs a second before it earns a rule.

## `<name TBD>`: how you arrived at the goal (the *why*)

The step before the goal. `definition-of-done` owns the *goal*, the *what* that must be true for a
change to be done; this owns the *why*: the problem, the evidence, and the reasoning that produced
that goal, so it can be trusted and revisited rather than taken as given. **Why before what:**
justify the goal before you state it.

Completes the chain **why → what → how**. The *what* has two faces: `spec` states the target and
`definition-of-done` confirms it was hit; both are the *what*, not two rungs. This skill is the
*why* above them; `decision-log` is the *how* below (and it records the why of a *decision*, a
narrower why than the why of the *goal*). `essays` carry some of this reasoning as narrative, but
are not the structured account.

**A why has a source, and the source is its weight.** Where the goal came from sets how much it must
earn its place before you build on it:
- *research*: evidence-backed; grounded, if the research holds.
- *an immediate problem*: real, if it is the root problem and not a symptom.
- *intuition or past learnings*: may be right, may be stale; unexamined until it is named.
- *someone asked or recommended*: an inherited why; whose problem is it, and did they examine it?
  (the bundler recommendation was this one.)
- *a lifelong dream*: motivating, but the weakest evidence that this is the right thing to build now.

None is disqualified. The weaker sources are a flag to validate the goal harder, not to skip it, and
the skill names the source so its weight is visible. Candidate spine: *a goal is only as trustworthy
as the why behind it; name where it came from.*

Name TBD: `rationale`, `problem`, `discovery`, `justification`, `why`. Open.

Prompted 2026-09-22: "dod is not the why, it's the what; how you arrived at the goal is the why."

## `linting`: enforce the rules mechanically from the first commit

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

### Selection procedure (agreed)

Ordered, not criteria to weigh. Each step is a question with a decision.

1. **Does the toolchain ship one?** If yes, that is the answer. Zero install, zero version drift,
   guaranteed compatibility, nothing added to the supply chain, and `simplicity` rule 6 already
   points here. Rust has clippy; Go has `go vet`. Stop unless step 3 disqualifies it.
2. **Has the ecosystem converged?** If the toolchain ships nothing, take the dominant tool rather
   than the best one. Deviating costs you plugins, documentation, and every answer written on the
   internet, which is a recurring tax for a marginal gain.
3. **Can it express the rules our skills require?** The disqualifying check, and the only one that
   overrides 1 and 2. Cognitive complexity, import boundaries, identifier denylist, naming regex,
   doc presence. A rule needing a plugin is fine; a rule nothing can express puts the tool out.
   This is usually where a fast newcomer fails, since speed often comes with thinner coverage.
4. **Fast enough to run on save?** Tie-breaker. Speed decides whether it runs locally or only in
   CI, and CI-only means finding out after you have moved on.
5. **Is there an escape hatch for a custom rule?** Tie-breaker. The skills will eventually require
   a rule nobody has written.

Output is a `decision-log` entry naming the tool and which step settled it, so the reasoning is
recoverable when someone proposes switching.

**Verify the tool examples before writing them into the skill.** clippy, `go vet`, ruff, oxlint
coverage claims are currently recalled, not cited, which is our own `platform-correctness` rule 1
pointed back at us.

### Day one becomes a branch, not a stance

Adopting at project start needs no decision. Adopting later forces one, because you must either
suppress the existing violations or fix them, and that choice gets logged. That turns "day one or
not at all" from a position into a procedure step. The day-one half is owned by `project-setup`.

## `test-fidelity`: a test must be able to fail for the real reason

Designed; one refinement recorded below (flow coverage). Five rules, each a way a test loses that
ability:

1. **Place the test at the seam.** A test far from the failure fails for a proxy reason. Unit
   tests where the logic is; contract tests at every service boundary, including local utilities
   and shell scripts, which is the part people skip.
2. **Cover every dimension; the e2e dimension covers the enumerated flows.** Unit, integration,
   e2e, browser. A missing kind means that class of failure cannot be caught at all. For e2e, the
   coverage target is the enumerated key user flows and their options, taken from the spec: each
   driven end to end, asserting the goal reached, not the lines touched. 100% of that list, since
   the flows are the spec's behavioral core. Presence across kinds, not the test pyramid's
   proportions.
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

### Flow coverage, and why it is a gate

The e2e gap in AI-built code is not industry's cost gradient; code is cheap. It is optimism: the
model assumes the flow works and never writes the test that would complete it. A bias, not a budget,
so the fix is a measured gate (100% of the enumerated flows), not a judgment call. That is the
`format` and `linting` move: take it out of judgment.

Ownership stays clean. Enumerating the flows and their options is high-leverage `spec` work: the
`spec` states the behavior, `test-fidelity` requires each enumerated flow exercised end to end and
asserting the goal. So "user flows" does not enter the general `spec` skill (a library API or a
data-format spec has no flows); it enters here, as the denominator this rule measures against.

Coverage here means execution against that denominator, not lines touched; line coverage inflates
because it is cheap to raise, and the user flow is the behavior it cannot count. The residual trust
question moves with it, and to a better place: not "are the assertions across the suite strong
enough" (opaque) but "did we enumerate the right flows" (one legible list, reviewable as spec).

## `glossary`: a domain concept has one registered term

Pulled out of `spec` (2026-09-22), so `spec` stays *what, at the right depth, before how* and the
vocabulary has its own home. Owns the *register* act in the chain **industry → glossary → code**:
adopt the established industry term for a domain concept, record it, and cite the source; coin a
term only for a construct with no industry name, and mark it as ours. One term per concept.

Three peers on the vocabulary chain: this *registers* the term, `spec` *uses* it to say what the
system does, `naming` *binds* code to it (rule 6). `naming` could absorb the register act, but its
spine ("a name tells the truth about the thing it names") is individual code names, not a domain
registry; a different act. Each glossary entry cites its source, per `platform-correctness` rule 1.

Name TBD: `glossary`, `define-terms`, `vocabulary`.

## `project-setup`: set up what is expensive to change later

Owns technology selection and standing up the gates before the first feature: language, build
tool, linter, formatter, test runner, CI, directory layout, licence, PR template.

**If you will do it twice, it is a checked-in command.** A task runner exists from the first
commit, and anything done by hand that will recur becomes a recipe in it at the moment of doing it
by hand, not afterwards. Capture, retest, rebuild, release. `pubnet-tools` is the reference: every
recipe committed, and each one commented with why it exists rather than what it runs.

**The sentence matters here.** "Everything you do at the start" is a *time* grouping, and time
groupings are usually a smell. The real category is the **cost curve**: choices whose switching
cost rises sharply after the first commit. That is why the language, the linter and the directory
layout belong together, and why adding a dependency in month three does not, since that is
`simplicity` rule 6.

Named `project-setup` rather than `scaffolding` because `contracts` needs that word for
wheelviser's meaning, a wrapper contract around an undocumented dependency, which is the more
valuable use.

Splits from siblings: `decision-log` owns how a decision is made and recorded, this owns *which*
decisions must be made before starting. `platform-correctness` owns conforming to a platform, this owns choosing
one. `linting` owns the mechanism, this owns standing it up on day one.

## `<name TBD>`: draw a spec out of the person who holds the intent

Decided 2026-09-24, from the spec-form analysis (#51): coaching is its own skill, not a part of
`spec`. `spec` owns what a spec says and its form; this owns getting it out of someone who knows
exactly what the behaviour should be and cannot write it down in that form. Candidate spine: *the
author's intent, in the author's words, checked by the author.*

Source material is MetanoiaFramework `spec`, "Drawing a spec out of someone", to be extracted, not
trimmed (0002):

- **Draft first, ask second.** Most of a spec is already in the conversation, unsorted. At most
  three questions in one message, aimed at the gaps.
- **The question ladder**, in order of yield: narrate it happening once; how would you check it
  worked; what must already be true; what kicks it off; the version where it goes wrong; what
  would make you say "that's not what I meant"; is there a number in this.
- **The failure families** for finding the failure scenario: too late or early, already happened,
  never happens, not allowed, missing or wrong input, simultaneous, partially done, wrong state.
- **Ask for corrections, not approval.** "Anything wrong or missing?" gets edits; "does this look
  good?" gets a reflexive yes.
- **The author's vocabulary, not the codebase's.** A spec its author cannot read back is a
  translation taken on faith.
- **The contract-drafting mapping** (conditions precedent, triggering event, obligation, carve-outs,
  definitions, conditions to closing), and where it breaks: no reasonableness standard, no
  adjudicator who infers intent.

**Who it is for: a spectrum, not a class of author** (settled 2026-09-24). Familiarity with specs
runs from none, through a junior engineer or someone who has programmed a little, to a senior
engineer, and even the far end rarely produces a high-quality spec solo. So the skill applies
whenever a person holds the intent, and calibrates to what they bring rather than switching on
for non-engineers. Consequences:

- **Coaching is the default way a spec gets written with a person**, not a remedial mode. The
  agent drafts and the author corrects, at every point on the spectrum.
- **Calibrate the questions, do not skip them.** Someone further along needs fewer of the basic
  questions (what kicks it off, what must be true first) and more of the probing ones (the failure
  families, "what would make you say that's not what I meant"), which catch what experience
  assumes.
- **Bridge from the frame the author already has.** The contract-drafting mapping is one bridge;
  test cases (Arrange, Act, Assert), user stories, and acceptance criteria are others. Pick the
  one they know, or none.

Prompted 2026-09-24: "i have tons of software engineering experience but wouldn't say i could
build an exact spec solo myself and produce a high quality artifact."

Name TBD. Requirements engineering's term for the act is *elicitation*, which 0006 favours; also
`spec-interview`, `drawing-out`.

## Also planned

`harness` (make the system locally observable without external services), `tdd` (port),
`error-taxonomy` (port).

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
