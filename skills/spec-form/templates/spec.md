---
slug: <slug> # lowercase-kebab-case, names the behaviour: dns-leak-detection, candidate-withdrawal
status: draft # draft | agreed | superseded | abandoned. draft while an open question bears on a scenario
owner: <name> # whose intent this records: the person to ask when a scenario reads two ways
date: YYYY-MM-DD # when first written; later changes live in version control
related: [] # repo-relative paths to the decisions, specs, and tickets this depends on or affects
---

# Spec: <title>

## Intent

What the person using the system can do once this holds, in one short paragraph of plain language.
No modules, endpoints, or data model: if a reader cannot tell what changes for the people using it,
it is not written yet.

**Not in scope:** the neighbouring behaviour this spec leaves alone, and where it is answered
instead.

## Terms

Only words a scenario would be ambiguous without: a precise meaning here that ordinary use does not
have, or one two people would read differently. Say what it is not, if it is easy to confuse.

- **<term>**: <what it means here, specifically enough to check>.

Delete this section if nothing needs defining.

## Shape

Only when part of the contract is data rather than behaviour (exit codes, a file or message
format, the fields another system reads): a table of it. Delete otherwise.

## Scenarios

At least one happy path and at least one failure or edge case. Mark each on its own line. IDs are
permanent: a new scenario takes the next unused number; a removed one's number is retired.

### S1: <what happens, in a few words>

**Happy path.** <Optional: the real case this came from, dated.>

- **Given** <what is already true: who exists, what state they are in, what has happened>
- **And** <another precondition>
- **When** <the single triggering event; a second one means a second scenario, or it is a Then>
- **Then** <the outcome, checkable by someone who was not there; an outcome, not a mechanism>
- **And** <another outcome>

### S2: <what happens when it goes wrong>

**Failure.**

- **Given** <the precondition that makes this the failure case>
- **When** <the trigger>
- **Then** <what the person is told, or what the system reports, specifically>
- **And** <what must not have happened: nothing recorded, nobody notified, no state changed>

### S3: <an edge case>

**Edge.**

- **Given** <...>
- **When** <...>
- **Then** <...>

## Open questions

What a scenario depends on that is not known yet. Never fill one with an invented answer.

- **<the question>**: <who can answer it, and what it blocks>.

Write `None outstanding.` when there are none.

## Resolved questions

A question once open, kept with its answer and when it was settled, so it is not asked again. A
question that chose between options is a decision record instead; link it here.

- **<the question>** <the answer>. *(Settled YYYY-MM-DD: <how, e.g. a spike or a capture>)*

Delete this section if there are none.

## Done when

Every scenario holding is implied; do not list them. List what no single scenario carries:

- <an invariant: what must never happen, in any scenario>
- <a cross-cutting bar: existing behaviour unaffected, a migration complete>

A line that traces to no scenario is either one of these or a scenario nobody wrote. Check which.

## Why this behaviour

Two or three sentences: the problem, and why it is shaped this way rather than the obvious
alternative. Link the decision record rather than restate it.
