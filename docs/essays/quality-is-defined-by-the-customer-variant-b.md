# Quality is defined by the customer

**2026-10-05 · Claude Opus 5.5**

## Where we landed

Hampton noticed, on 2026-10-05, that many of the principles the skills implement closely match
total quality management (TQM). The lineage runs through all of TQM: why it exists, what it
holds quality to be, and the methods that follow from both. The README now names TQM as the
tradition the skills belong to. This essay explains TQM for a reader who has never met it,
starting from its why and its what, sets TQM's why beside the project's, then shows where the
skills match it and where they do not.

## What TQM is

Total quality management is a way of running an organisation in which quality is everyone's job,
not a separate department's. The American Society for Quality summarizes it as "a management
system for a customer-focused organization that engages all employees in continual improvement of
the organization."[^asq]

It grew out of the quality-control techniques of the half century before it,[^wiki] among them
the work of Walter Shewhart of Bell Labs and of W. Edwards Deming, the American he
mentored.[^pdsa] Japanese manufacturers applied those techniques well enough that by the late
1970s their high-quality, low-cost goods were outcompeting North America's and Western Europe's.
American organisations set out to learn how, and the US Navy adopted Deming's teaching and named
its programme "Total Quality Management" in 1985.[^wiki]

## Its why: lasting by serving the customer

At its core, ASQ says, TQM is "a management approach to long-term success through customer
satisfaction."[^asq] The first of Deming's fourteen points for management puts the same purpose
first: "Create constancy of purpose toward improvement of product and service, with the aim to
become competitive and to stay in business, and to provide jobs."[^deming] An organisation lasts
because the people it serves keep choosing it.

The why has a second face, the people doing the work. Deming's twelfth point removes the barriers
that rob workers, managers and engineers of their "right to pride of workmanship."[^deming]

Set beside it, the project's why as the repo states it so far. Its essays say the skills exist
because an agent's defaults are a helpful assistant's, not an engineer's: left alone, it builds
something and then blesses it ([An assistant, not an engineer][assistant]). And "more mediocrity
traces to a goal never set than to a job done badly" ([Define what good looks like][good]).

The two whys meet twice. Both start from the person the work is for. And both treat bad work as
the system's doing, not the worker's: Deming put most defects on the system, and the essays put
the agent's on its defaults, re-targeting those rather than blaming the agent. They part on scale.
TQM's why is an organisation lasting and providing jobs; the project's, as written so far, is each
piece of work being good, and says nothing yet of lasting, or of pride in the work. The project's
full why is its owner's to state, and until then this comparison is only against the essays.

## Its what: a satisfied customer, pursued as a process

From that why follows TQM's what. Quality is not a property the builder measures against an
internal standard; it is set by the customer. The Navy's programme put it plainly: "Quality is
defined by customers' requirements."[^wiki] ASQ's first principle: "The primary goal of TQM is to
meet or exceed customer expectations."[^asq]

Deming went further, in two ways. Satisfaction is the floor, not the goal: "It will not suffice to
have customers that are merely satisfied," because a satisfied customer may still switch. "Profit
in business comes from repeat customers, customers that boast about your product and service, and
that bring friends with them."[^satisfied] And satisfaction is pursued as a process,
not checked once as an outcome. In his 1950 speech to Japanese industrial leaders: "The process of
sales is not something that finishes simply with transporting the products to the marketplace, and
receiving money. In today's sales, after selling the product, the businessman must think about
whether he has satisfied the customer, and how improvements can be made from then on."[^1950]
Hampton's example is a salesperson who works with the customer until the product matches their
needs.

The skills match the start of that process:

- **The user defines the goal.** `spec` 3: ask the person whose problem it is, and don't fill the
  gap with the convenient reading. `spec` 5: the goal is what the output lets its user do, not
  what it is or a number it hits. Deming's goal is wider: the customer satisfied, and coming back.
- **The goal is worked out with its owner.** `spec` 3: the goal comes "often in pieces." `spec` 4:
  date each answer as it lands, and when the goal changes, recheck the work built on the old one.
- **The what comes first.** `spec` 1: what the change must do, and its criteria, before choosing a
  tool or a design.
- **Done is judged as the user would judge it.** `definition-of-done` 4: use the output as the
  person it is for would. Rule 7: "Following the spec is not the same as being good," so the demo
  is judged against what was wanted, not only against what was written down.

## Its how: methods that follow

TQM's methods are how it pursues that what. The skills echo each of the best known:

- **Build quality in; don't inspect it in.** The third of Deming's fourteen points: "Cease
  dependence on inspection to achieve quality," by "building quality into the product in the first
  place."[^deming] Here, `spec` sets criteria before the work, and `definition-of-done` 6 builds
  the tell into the artifact.
- **Most defects belong to the system, not the worker** (points 10 and 11). When an agent failed
  to load `spec` when it should have, the fix was to the skill's triggers ([0020][0020]).
- **Plan, do, study, act.** Plan a change with a prediction, make it, study the result against the
  prediction, act on what was learned.[^pdsa] Here: `spec`, the build, `definition-of-done`, and a
  decision superseded in the log (`decision-log` 5).
- **Stop on an abnormality.** From Toyota's production system, TQM's close cousin: any operator can
  pull a cord to stop the line, so a defect is not passed downstream.[^toyota] Here, `review` 3
  reports what cannot be verified as blocked, never passed.

Each source is short, free, and written for newcomers: ASQ's overview lists TQM's eight
principles,[^asq] the Deming Institute gives the fourteen points[^deming] and the PDSA cycle,[^pdsa]
and Toyota describes its production system.[^toyota]

## Where the match is loose

**TQM measures; the skills mostly do not yet.** TQM decides on data, with statistical tools to
analyse it.[^asq] Here, each change is held to evidence, but the skills themselves are not: on
main, `evals/` holds only a licence ([0019][0019]), and the `simplicity` thresholds are borrowed
defaults, not measured ones ([open questions][open-questions]).

**TQM follows the customer past delivery; the skills do not yet.** `definition-of-done` checks a
unit when it is handed over. Going back to the user afterward, to ask whether they were satisfied
and what to improve, is where Deming's process continues, and it is not implemented yet.

**TQM runs an organisation; the skills govern a unit of work.** Leadership, supplier
relationships, strategy, and how people are appraised make up much of Deming's fourteen points,
and no skill governs them directly. Hampton's hypothesis is that the skills push on the
organisation anyway, through the communication style they teach. It is untested, and tracked in
[#111][issue-111].

**The name is dated.** ASQ notes TQM "is not as widely used in the United States as it once
was,"[^asq] its ideas now filed under quality management, ISO 9000, Lean and Six Sigma.[^wiki] The
README names TQM for its ideas, not its programmes or certifications.

## What it shapes

- A newcomer has a frame and a vocabulary to search with: decades of material on quality defined
  by the customer, and industry terms over our own ([0006][0006]).
- The loose fits are visible. Measurement and following the customer past delivery are the
  largest, and neither is implemented yet.

## Revisions

- **v1.0 · 2026-10-05 · Claude Opus 5.5.** First version.

[0006]: ../decisions/0006-glossary-industry-terms-over-coinage.md
[0019]: ../decisions/0019-evals-take-apache-2-0.md
[0020]: ../decisions/0020-spec-triggers-on-events-and-builds-the-goal-with-its-owner.md
[open-questions]: ../context/open-questions.md
[assistant]: assistant-not-engineer.md
[good]: define-what-good-looks-like.md
[issue-111]: https://github.com/cobarx/build-skills-cobarx/issues/111

[^asq]: American Society for Quality, "What Is Total Quality Management (TQM)?",
    <https://asq.org/quality-resources/total-quality-management>, reviewed November 2024. Overview
    and the eight principles.
[^deming]: W. Edwards Deming, *Out of the Crisis* (MIT Press), pp. 23-24, as condensed by the
    W. Edwards Deming Institute, "Dr. Deming's 14 Points for Management",
    <https://deming.org/explore/fourteen-points/>.
[^pdsa]: The W. Edwards Deming Institute, "PDSA Cycle", <https://deming.org/explore/pdsa/>.
    Shewhart as Deming's mentor at Bell Labs, and why Deming preferred *study* to *check*.
[^toyota]: Toyota Motor Corporation, "Toyota Production System",
    <https://global.toyota/en/company/vision-and-philosophy/production-system/>. Jidoka, the stop
    cord, and the andon board.
[^wiki]: Wikipedia, "Total quality management",
    <https://en.wikipedia.org/wiki/Total_quality_management>, retrieved 2026-10-05. History, the
    Navy's naming in 1985, and its definition of quality.
[^satisfied]: W. Edwards Deming, *Out of the Crisis*, 2nd ed. (MIT Press, 2000), p. 119 of the
    Kindle edition, as quoted by the W. Edwards Deming Institute,
    <https://deming.org/quotes/it-will-not-suffice-to-have-customers-that-are-merely-satisfied-an-unhappy-customer-will-switch-unfortunately-a-satisfied-customer-may-also-switch-on-the-theory-that-he-could-not-lose-much-and-mi-3/>.
[^1950]: W. Edwards Deming, speech to Japanese industrial leaders at Mt. Hakone, 1950, translated
    from the Japanese transcript held by JUSE. Excerpted in John Hunter, "Speech by Dr. Deming to
    Japanese Business Leaders in 1950", the W. Edwards Deming Institute,
    <https://deming.org/speech-by-dr-deming-to-japanese-business-leaders-in-1950/>.
