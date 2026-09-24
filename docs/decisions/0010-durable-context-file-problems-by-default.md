# 0010. A problem you notice is filed by default

- **Status:** Accepted
- **Decided:** 2026-09-24 (#44) · **Recorded:** 2026-09-24 · Claude Opus 5.5
- **Affects:** `durable-context`

## Context

On a pubnet-tools session an agent found four real problems while doing other work (a scoring
false alarm, an undetected filter, a broken fixture path, a network-dependent unit test), listed
them in chat, and asked whether to open issues. The dev's answer was that filing should have been
the default. `durable-context` rule 2 covered where deferred work goes once someone decides to
record it; nothing said a noticed problem must be recorded at all.

## Options

- **Ask before filing.** The prior behaviour. Every finding becomes a question the dev has to
  answer, and one left unanswered stays in a chat that ends.
- **File by default; the agent judges whether the dev already knows.** Fewer redundant issues, but
  the agent is guessing, and a wrong guess drops a problem silently.
- **File by default; the dev declares what not to file.** Early in a project the dev can name areas
  not expected to work yet, at the entry point or in the moment, and those go unfiled.

## Decision

The third. An unneeded issue costs a close; a lost problem costs rediscovering it, usually later
and in a worse place. Severity or fix still open is not a reason to wait, since the issue is where
that discussion belongs. The early-project exception is real (the dev said so: issues for things
not expected to work yet are noise), and declaring it keeps the decision with the person who holds
the knowledge.

## Consequences

- `durable-context` gains rule 6, and its description gains the trigger so it loads on noticing a
  problem, not only on recording one.
- Issues inherit whatever the project says about publishing (a public repo's scrub policy applies
  to an issue body as much as to a commit).
