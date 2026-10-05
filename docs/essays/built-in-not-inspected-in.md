# Built in, not inspected in

**2026-10-05 · Claude Opus 5.5**

## Where we landed

Hampton, 2026-10-05: "many of the principles that this repo is designed to implement are a close
match with TQM." Read against total quality management, most of the skills restate one of its
principles for a single unit of work. The README now names TQM as the tradition the skills belong
to. This essay explains TQM for a reader who has never met it, shows where the skills match it, and
says where they do not.

## What TQM is

Total quality management is a way of running an organisation in which quality is made by the
process and is everyone's job, rather than checked at the end by a separate department. The
American Society for Quality summarizes it as "a management system for a customer-focused
organization that engages all employees in continual improvement of the organization."[^asq]

It grew out of the quality-control techniques of the half century before it,[^wiki] among them
the work of Walter Shewhart of Bell Labs and of W. Edwards Deming, the American he
mentored.[^pdsa] Japanese manufacturers applied those techniques well enough that by the late
1970s their high-quality, low-cost goods were outcompeting North America's and Western Europe's.
American organisations set out to learn how, and the US Navy adopted Deming's teaching and named
its programme "Total Quality Management" in 1985.[^wiki]

Four ideas carry most of it, the last from Toyota's production system, TQM's close cousin:

- **Build quality in; don't inspect it in.** Inspection at the end finds a defect after it is
  made. The third of Deming's fourteen points for management: "Cease dependence on inspection to
  achieve quality," by "building quality into the product in the first place."[^deming]
- **Most defects belong to the system, not the worker.** So the fix is to the process, not
  exhortation: Deming would drop slogans and numerical targets for the workforce (points 10 and
  11).
- **Plan, do, study, act.** Plan a change with a prediction of what it will do, make it, study the
  result against the prediction, and act on what was learned. Then go round again.[^pdsa]
- **Stop on an abnormality.** On a Toyota line any operator can pull a cord to stop the line when
  something is wrong, so a defect is not passed downstream. Toyota calls this jidoka.[^toyota]

Each source is short, free, and written for newcomers: ASQ's overview lists TQM's eight
principles,[^asq] the Deming Institute gives the fourteen points[^deming] and the PDSA cycle,[^pdsa]
and Toyota describes its production system.[^toyota]

## Where the skills match

ASQ's eight principles, against the skills:

| Principle | In the skills |
|---|---|
| Customer focused | `spec` 5: the goal is what the output lets its user do. `definition-of-done` 4: use the output as the person it is for would. |
| Employee involvement | Quality is the author's job, person or agent: the author shows the goal met (`definition-of-done`) before a reviewer looks. Anyone doing the work can stop the line (below). |
| Process approach | The skills govern how a unit of work is sized, specified, reviewed and shown done, not what any product does. |
| Integrated system | The skills' "Not here" sections hand each concern to its owner; `spec`'s criteria feed `definition-of-done` and `decision-log` (`spec` 7). |
| Strategic and systematic approach | No counterpart (see below). |
| Continual improvement | Decisions are superseded, never edited (`decision-log` 5); essays log their revisions (`essays` 2). |
| Fact-based decision making | `definition-of-done` 1: the measured value beside the expected one. `decision-analysis` 3: measure, do not recall. |
| Communications | `durable-context`: context lives in the project, in the open. `decision-log`: a decision is reasoned in the open. |

The four ideas map as closely:

- **Built in.** `spec` sets the criteria before the work starts, `simplicity` keeps each change
  cheap enough to check, and `definition-of-done` 6 builds the tell into the artifact so a defect
  shows itself. `review` remains, but checks against a standard declared in advance (`review` 2).
- **The system, not the worker.** When an agent failed to load `spec` at the moment it should
  have, the fix was to the skill's triggers ([0020][0020]), not a reprimand in that one session.
  The `simplicity` thresholds are "diagnostics, not targets": a number used to notice a problem,
  never set as a goal (point 11).
- **PDSA.** Plan is `spec`, its criteria the prediction. Do is the build. Study is
  `definition-of-done`: the measured value beside the expected one, and a goal refined by what was
  learned is "the process working" (`spec` 5). Act is changing the goal or the method on what was
  learned, recorded as a decision that supersedes the old one (`decision-log` 5).
- **Stop the line.** `review` 3: what cannot be verified is reported blocked, never passed.
  `durable-context` 6: a problem noticed on the way is filed before the work moves on.

## Where the match is loose

**TQM measures; the skills mostly do not yet.** TQM decides on data, with statistical tools to
analyse it.[^asq] Here, each change is held to evidence, but the skills themselves are not: on
main, `evals/` holds only a licence ([0019][0019]), and the `simplicity` thresholds are borrowed
defaults, not measured ones ([open questions][open-questions]).

**TQM runs an organisation; the skills govern a unit of work.** Leadership, supplier
relationships, strategy, and how people are appraised make up much of Deming's fourteen points and
have no counterpart here. A skill an agent loads for one change cannot set a company's strategy.

**The name is dated.** ASQ notes TQM "is not as widely used in the United States as it once
was,"[^asq] its ideas now filed under quality management, ISO 9000, Lean and Six Sigma.[^wiki] The
README names TQM for its ideas, not its programmes or certifications.

## What it shapes

- A newcomer has a frame and a vocabulary to search with: decades of material on why building
  quality in beats inspecting it in, and industry terms over our own ([0006][0006]).
- The loose fits are visible. Measurement is the largest, and it is where the skills are weakest
  by TQM's own standard.

## Revisions

- **v1.0 · 2026-10-05 · Claude Opus 5.5.** First version.

[0006]: ../decisions/0006-glossary-industry-terms-over-coinage.md
[0019]: ../decisions/0019-evals-take-apache-2-0.md
[0020]: ../decisions/0020-spec-triggers-on-events-and-builds-the-goal-with-its-owner.md
[open-questions]: ../context/open-questions.md

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
    <https://en.wikipedia.org/wiki/Total_quality_management>, retrieved 2026-10-05. History, and the
    Navy's naming in 1985.
