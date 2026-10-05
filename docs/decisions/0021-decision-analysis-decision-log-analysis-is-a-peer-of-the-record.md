# 0021. Decision analysis is a peer skill of the decision log

- **Status:** Accepted
- **Decided:** 2026-10-04 · **Recorded:** 2026-10-04 · Claude Opus 5.5
- **Affects:** `decision-analysis` (new), `decision-log` (a pointer only)

## Context

Hampton asked for a decision-analysis skill and supplied the test case: whether apotheosis builds
with Fedora's Rust packages or rustup. He wanted the pros and cons of both, written to a Markdown
file he could read outside the agent, because rustup moves a core tool outside the operating
system's management and he wanted to see the compelling reasons before accepting that. The
analysis is `docs/context/toolchain-analysis.md` in apotheosis, a repo not yet published.

Two rounds of correction came from that case. First, the reply added a summary and proposals
beside the file: "you don't get to add context. period. you created an analysis. that's it. if you
need to say extra, why didn't you put it in the analysis." He then allowed a collapsed copy of the
analysis inline. Second, on reading it: "the first thing i'm wondering when reading this is why
rustup exists and why it wants to manage things separately. that's not apparent in the first part
of the doc"; the analysis said rust-lang.org recommends rustup "then don't specify why they say
this"; and "a tl;dr in the analysis would also be helpful."

## Options

- **Extend `decision-log`.** Its rule 1 (frame before choosing) and rule 3 (no raw menu, give a
  recommendation) already reach into analysis. Rejected on the owner's distinction: "decision log
  is a record of a decision, analysis has to be performed first." A record and the work it records
  are read at different times, by different readers.
- **Fold into `spec`.** `spec` sets the criteria, but says nothing about measuring options against
  them or presenting the result to a decider.
- **A peer skill.**

## Decision

A peer skill, `decision-analysis`. The name is the industry term: Ronald A. Howard coined
*decision analysis* in "Decision Analysis: Applied Decision Theory" (1966). The skill adopts the
term and the discipline's aim, translating the analysis into insight for the decision maker. It
does not adopt the formal method (decision trees, expected utility), which is out of proportion to
the choices this library meets (`adopting-standards` rule 5).

The rules are the ones the test case needed:

- The decider's objection is a criterion, weighed and not argued away (rustup as an anti-standard).
- Facts are measured, with how and when: Fedora's packaging dates from the RPM changelog against
  upstream release notes, not a recollection that distributions lag.
- An authority's recommendation is given with its reason (the second correction).
- The disliked option gets its strongest case, starting with why it exists (the second
  correction), each argument marked as applying now or not.
- One recommendation, with the conditions that would reverse it.
- A summary opens the analysis (the second correction; the industry name is an executive summary).
- The analysis stands alone; the reply is its path (the first correction). A copy only where it
  shows collapsed: in the terminal a `<details>` block printed in full, and the owner's answer was
  "i said collapsed. if that can't be done, don't print it." Revised in review on 2026-10-05,
  before merge: the reply may repeat the file's opening summary ("i'm not opposed to the summary
  being the reply"), so long as it says nothing the file does not. Three runs of that wording kept
  every reply true to its file but none to its summary: each wrote a longer digest, adding the
  reversal conditions and caveats. The owner then settled it: "it should only be the file's summary
  and the path." The collapsed copy goes with it.

## Consequences

- `decision-log` gains only a "Not here" pointer. Its rules 1 and 3 overlap the new skill; whether
  they move is a separate change (#73).
- The analysis lives where `durable-context` puts unsettled work (`docs/context/`) until the
  decision is recorded.
- Adding a skill is a minor bump.
