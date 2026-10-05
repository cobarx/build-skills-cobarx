# 0021. Decision analysis is a peer skill of the decision log

- **Status:** Accepted
- **Decided:** 2026-10-04 · **Recorded:** 2026-10-04, revised in review 2026-10-05 · Claude Opus 5.5
- **Affects:** `decision-analysis` (new), `decision-log` (a pointer only)

## Context

The owner asked for a decision-analysis skill and supplied the test case: whether one of the
owner's Rust projects, not yet published, builds with Fedora's Rust packages or with rustup. The
owner wanted the pros and cons in a Markdown file readable outside the agent, because rustup moves
a core tool outside the operating system's management, and wanted to see the compelling reasons
before accepting that.

Two rounds of correction came from that case. First, the reply added a summary and proposals
beside the file: "you don't get to add context. period. you created an analysis. that's it. if you
need to say extra, why didn't you put it in the analysis." Second, on reading it: "the first thing
i'm wondering when reading this is why rustup exists and why it wants to manage things separately.
that's not apparent in the first part of the doc"; the analysis said rust-lang.org recommends
rustup "then don't specify why they say this"; and "a tl;dr in the analysis would also be helpful."

## Options

- **Extend `decision-log`.** Its rule 1 (frame before choosing) and rule 3 (no raw menu, give a
  recommendation) already reach into analysis. Rejected on the owner's distinction: "decision log
  is a record of a decision, analysis has to be performed first." A record and the work it records
  are read at different times, by different readers.
- **Fold into `spec`.** `spec` sets the criteria, but says nothing about measuring options against
  them or presenting the result to a decider.
- **A peer skill.**

## Decision

A peer skill, `decision-analysis`. The name is the industry term, coined by Ronald A.
Howard.[^howard] The skill adopts the term and the discipline's aim, translating the analysis into
insight for the decision maker. It does not adopt the formal method (decision trees, expected
utility), which is out of proportion to the choices this library meets (`adopting-standards`
rule 5).

The rules, and where each came from:

1. **Criteria first, objections included.** The test case: rustup as an anti-standard, weighed
   rather than argued away.
2. **Ask what only the decider can settle.** Review: two runs quietly widened the objection
   ("outside the OS package manager" became "outside apt or snap"). The owner: "when in doubt,
   ask. the decision analysis helps form the spec. you need clarity on unknowns." "When in doubt"
   alone changed nothing, because the model is not in doubt (the trigger problem 0020 fixed for
   `spec`), so the rule names an observable trigger: an option that meets the objection only
   under a reading broader than the decider's words. Questions go in the summary, so they reach
   the decider through rule 11.
3. **Measure, do not recall.** The test case: Fedora's packaging dates from the RPM changelog, not a
   recollection that distributions lag, because ecosystems move faster than memory. Review added
   "never claim blanket verification" after a run claimed every fact was fetched while stating two
   from memory.
4. **An authority's reason, not only its verdict.** The second correction.
5. **Steelman the resisted option, starting with why it exists.** The second correction: its
   purpose is the decider's first question, and a decider who sees why each argument holds or
   fails can trust the recommendation or overturn it. "Steelman" is the industry term for
   building the strongest version of the opposing case (0006); this rule adds the purpose first
   and a verdict on each argument.
6. **Recommend one.** Review: runs hedged with a preference-based second pick, traced to a criterion
   the recommendation lost on without saying why. So it must say why it still wins, and a
   preference only the decider holds becomes a question (rule 2). The owner: "an improvement" that
   "feels incomplete"; #95 carries it.
7. **Say what would reverse it.** Observable conditions turn a later reversal from a re-argument
   into a check.
8. **Open with a summary.** The second correction ("a tl;dr"; the industry name is an executive
   summary), so the decider can stop there or read on knowing where it leads.
9. **The analysis stands alone.** The first correction.
10. **Reread the file before replying.** Review: a blanket verification claim and a second pick
    each survived a rule against it, because nothing made the model reread.
11. **The reply is the summary and the path.** The first correction, then settled in review. The
    owner allowed the summary ("i'm not opposed to the summary being the reply"), then narrowed
    it: "it should only be the file's summary and the path." A collapsed copy, allowed at first,
    was dropped: a terminal printed it in full ("i said collapsed. if that can't be done, don't
    print it").

## Evidence

Headless runs on a different case from the one the skill was drawn from (Node on Ubuntu 24.04,
apt or nvm, with the decider objecting to nvm), three per wording, the reply checked mechanically
against the file's summary:

| Reply rule wording | Result |
|---|---|
| "may repeat the file's opening summary, but says nothing the file does not" | true to the file 3/3; limited to its summary 0/3 |
| "the file's opening summary, copied rather than rewritten" | verbatim 1/3; nothing else 0/3 |
| "paste the file's summary exactly as written, then its absolute path on its own line. No other information, caveats included" | 3/3, held through every later round |

The final eleven rules, graded blind on three runs: criteria, best case, reversal and summary
3/3; one recommendation 2/3, one borderline; asking, facts and an authority's reason each mixed,
with at least one fail. Every round and its grade is in #76.

## Consequences

- `decision-log` gains only a "Not here" pointer. Its rules 1 and 3 overlap the new skill; whether
  they move is a separate change (#73).
- The analysis lives where `durable-context` puts unsettled work (`docs/context/`) until the
  decision is recorded.
- Rules 2, 3, 4 and 6 are not yet reliable; #95 carries them, with the open question of asking
  before analysing.
- Adding a skill is a minor bump.

[^howard]: Ronald A. Howard, "Decision Analysis: Applied Decision Theory," *Proceedings of the
    Fourth International Conference on Operational Research* (1966).
