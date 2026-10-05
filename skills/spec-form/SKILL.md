---
name: spec-form
description: This skill should be used when writing, amending, or citing a spec; when a test or a change refers to a spec's scenario; when a scenario's outcome is about to change; or when a spec is about to carry a number nobody confirmed. It governs how a spec is written down, not what it must say or how deeply.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills-cobarx/tree/main/skills/spec-form"}
---

# spec-form

Write a spec so that someone who was not there can check every line of it.

`spec` decides what must be said and how deeply. This decides the form it is said in, so a builder
reads it one way and a test can cite it.

## Rules

1. **One behaviour, one spec, from the [template](templates/spec.md).** Search the existing specs
   first and amend the one that covers it; two specs for one behaviour make the builder guess.

2. **Scenarios are Given, When, Then, with one When.** The Then is an outcome someone absent could
   check, never a mechanism, unless the interface is the requirement. A contract that is data (exit
   codes, a field shape) is a table beside the scenarios.

3. **Every spec has a failure or edge scenario.** A failure's Then also says what did not happen.
   The error path left unwritten still gets decided, silently, by whoever builds it.

4. **Scenario IDs are permanent.** `<slug>#S<n>`, never renumbered or reused. Cite the ID rather
   than restate it, and find what cites a scenario before changing its Then.

5. **An unknown is an open question, never an invented number.** A spec stays `draft` while one
   bears on a scenario. A settled question keeps its answer in the spec, unless it chose between
   options: that is a `decision-log` entry.

6. **The spec changes with the behaviour, in place.** When the world contradicts it, amend it
   before the code.

7. **Done when holds what no scenario carries:** invariants ("never") and cross-cutting bars, each
   checkable. A line that traces to no scenario is either such a bar or a missing scenario.

## Not here

What a spec must say, and how deeply, is `spec`. Registering the terms it uses is `glossary`
(planned). Whether the goal was met is `definition-of-done`. This form was adopted under
`adopting-standards`. Turning a scenario into a test is `tdd` (planned).

---

Decisions affecting this skill: `docs/decisions/*-spec-form-*.md`
