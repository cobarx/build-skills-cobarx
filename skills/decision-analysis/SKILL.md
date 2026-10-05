---
name: decision-analysis
description: This skill should be used when someone has to choose between options and wants them weighed; when asked for pros and cons, a comparison of approaches, or an analysis before deciding; when the decider distrusts one option and wants to see the case for it; or before a decision is recorded. It governs performing the analysis a decision is made from, not recording the decision.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills-cobarx/tree/main/skills/decision-analysis"}
---

# decision-analysis

Give the decider what they need to weigh a choice themselves.

The analysis comes first and the record after. A decider handed a verdict can only trust it; one
handed the analysis can check it, and can disagree for reasons the analyst did not have.

## Rules

1. **The decider's criteria come first, objections included.** A preference or an unease the
   decider brings is a criterion. State it in their terms and weigh it like the others; do not
   argue it away. The rest come from the goal (`spec`).

2. **Ask what only the decider can settle.** An unknown the decider can settle is a question, not
   an assumption. Ask when in doubt, and always when an option meets an objection only under a
   reading broader than the decider's own words. Put the questions in the summary.

3. **Measure, do not recall.** Every fact the choice turns on comes from the system in front of
   you or a primary source, with how and when it was obtained. A remembered fact is a lead to check,
   and ecosystems move faster than memory. Mark any fact left unchecked; never claim blanket
   verification. When an authority recommends an option, give its reason, not only its verdict.

4. **Make the best case for the option the decider resists, starting with why it exists.** The
   problem it was built to solve comes first, because it is the decider's first question. Then give
   its strongest arguments their full weight, and say of each whether it applies to this work now.
   A decider who sees why each argument holds or fails can trust the recommendation, or overturn it.

5. **Recommend one, and say what would reverse it.** End with a single recommendation and the
   observable conditions under which it should be revisited. Those conditions are what turn a
   later reversal from a re-argument into a check. Where it loses on a criterion, say why it still
   wins. No second pick: a preference only the decider holds is a question for them (rule 2).

6. **Open with a summary.** The recommendation and the few reasons that decide it, before any
   detail, so the decider can stop there or read on knowing where it leads.

7. **The analysis stands alone.** Write it as a plain file the decider can read without the agent,
   including what could not be checked.

8. **Reread the file before replying.** Look for a claim of verification broader than what was
   checked, a second pick, and a criterion the recommendation loses on without saying why. Fix the
   file, not the reply.

9. **The reply is the summary and the path.** Paste the file's summary exactly as written, then its
   absolute path on its own line. No other information, caveats included; every detail is in the
   file.

## Not here

Recording the decision once made is `decision-log`. Where the analysis file lives is
`durable-context`. The goal the criteria come from is `spec`. Whether to adopt a standard is
`adopting-standards`; which layer's convention wins is `platform-correctness`. This governs
performing the analysis, not making or recording the decision.

---

Decisions affecting this skill: `docs/decisions/*-decision-analysis-*.md`
