# One incident is not a rule

**2026-09-20**

## Where we landed

`simplicity` has seven rules. An eighth was drafted three times and dropped. Rule 1 stands
unchanged. The lesson lives here instead.

## The incident

A probe script for YouTube was written as one unit and did five separable jobs: media stats,
listing native text tracks, enumerating the player object's methods, finding caption containers,
and resolving the fullscreen target.

It passed rule 1. The sentence was *show what the browser exposes about a playing video*, which is
true, contains no "and", and covers all five without strain.

## Three attempts at a rule 8

1. **"Bounded is not minimal."** Named a symptom and gave nothing to act on.
2. **"Count the jobs, not the sentence."** Right diagnosis, including that the cost of bundling
   falls on the reviewer rather than the builder. Still a second test for oneness standing beside
   rule 1.
3. **"One unit, one depth."** Survey and dive are different units; mixing them widens a unit
   without failing rule 1. The sharpest of the three, and still not integrated.

An intermediate version, *name a job, not a category*, was worse than useless: it would have
forbidden the survey, which is a legitimate unit on its own.

## What killed it

Reading the skill whole. Rules 1 through 7 each do different work: test for oneness, placement,
anti-merge, scoping, gate response, cost admission, behaviour under pressure. Every candidate rule
8 was a second test for oneness, sitting next to rule 1 and doing rule 1's job with a different
lens. It was not integrating with anything.

Rule 1 had also already caught it. Its caveat says an abstraction invented to make the sentence
work is a failure, not a pass. The probe was written first and described afterwards, so the
sentence was fitted to the code. The caveat fired and was ignored.

## Takeaways

- **One incident is not a rule.** It is an essay. A rule generalises from a pattern, and one data
  point is not a pattern.
- **Churn is the signal.** Three rewrites in three messages meant the general shape was unknown,
  only the specific instance. That should have stopped the third attempt before it was written.
- **Review the whole before adding to it.** A candidate rule can only be judged against the rules
  already there, and this one was only visibly redundant in context.
- **Check whether an existing rule already covers it.** Rule 1's caveat did. The failure was in
  applying it, not in the rule.
- **A rule that forbids a legitimate unit is worse than no rule.** "Name a job, not a category"
  would have banned reconnaissance.

## Open questions

- **Is survey-then-dive a real pattern?** It was useful here: survey first because it is cheap and
  tells you which dive is worth doing. Whether that generalises past one probe is unknown.
- **Does rule 1's caveat need more prominence?** It fired and was missed. That may be a wording
  problem, or may just be the ordinary cost of writing code before describing it.
- **Is `simplicity` already scope-drifted?** Rules 2 and 6 are placement and cost admission, not
  size. Both are useful; neither is "bound the size of a unit of work."
