---
name: decision-analysis
description: This skill should be used when someone has to choose between options and wants them weighed; when asked for pros and cons, a comparison of approaches, or an analysis before deciding; when the decider distrusts one option and wants to see the case for it; or before a decision is recorded. It governs performing the analysis a decision is made from, not recording the decision.
---

# decision-analysis

Give the decider what they need to weigh a choice themselves.

The analysis comes first and the record after. A decider handed a verdict can only trust it; one
handed the analysis can check it, and can disagree for reasons the analyst did not have.

## Rules

1. **The decider's criteria come first, objections included.** A preference or an unease the
   decider brings is a criterion. State it in their terms and weigh it like the others; do not
   argue it away. The rest come from the goal (`spec`).

2. **Measure, do not recall.** Every fact the choice turns on comes from the system in front of
   you or a primary source, with how and when it was obtained. A remembered fact is a lead to check,
   and ecosystems move faster than memory. When an authority recommends an option, give its reason,
   not only its verdict.

3. **Make the best case for the option the decider resists, starting with why it exists.** The
   problem it was built to solve comes first, because it is the decider's first question. Then give
   its strongest arguments their full weight, and say of each whether it applies to this work now.
   A decider who sees why each argument holds or fails can trust the recommendation, or overturn it.

4. **Recommend one, and say what would reverse it.** End with a single recommendation and the
   observable conditions under which it should be revisited. Those conditions are what turn a
   later reversal from a re-argument into a check.

5. **Open with a summary.** The recommendation and the few reasons that decide it, before any
   detail, so the decider can stop there or read on knowing where it leads.

6. **The analysis stands alone; the reply is its path, and at most its summary.** Write it as a
   plain file the decider can read without the agent, including what could not be checked. The
   reply gives the file's absolute path and may repeat the file's opening summary, but says nothing
   the file does not. A full copy goes in only where the reader's surface can collapse it.

## Not here

Recording the decision once made is `decision-log`. Where the analysis file lives is
`durable-context`. The goal the criteria come from is `spec`. Whether to adopt a standard is
`adopting-standards`; which layer's convention wins is `platform-correctness`. This governs
performing the analysis, not making or recording the decision.

---

Decisions affecting this skill: `docs/decisions/*-decision-analysis-*.md`
