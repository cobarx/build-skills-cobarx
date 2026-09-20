# The sentence test passes wide units

**2026-09-20**

## Where we landed

`simplicity` rule 1 does not stop a unit that does many things under one honest description. Three
attempts to close that were drafted and rejected. **The hole is recorded here, not patched.**

## The evidence

A probe script for YouTube was written as one unit and did five separable jobs: media stats,
listing native text tracks, enumerating the player object's methods, finding caption containers,
and resolving the fullscreen target.

It passed rule 1 cleanly. The sentence was *show what the browser exposes about a playing video*:
true, no "and", and it covers all five without strain.

## Why the caveat does not save it

Rule 1 ends with "an abstraction invented to make the sentence work is a failure, not a pass." It
is tempting to say the caveat fired and was ignored.

It did not. That sentence was not invented to pass a test. It is an accurate description of what
the code did, arrived at honestly. The caveat catches a sentence stretched to fit; it does nothing
about a sentence that fits because the umbrella is genuinely that wide.

**So the rule has a hole: any number of jobs passes, provided they share one true description.**

## Three attempts at closing it

1. **"Bounded is not minimal."** Named a symptom, gave nothing to act on.
2. **"Count the jobs, not the sentence."** Right about the cost falling on the reviewer rather
   than the builder. Still a second test for oneness standing beside rule 1.
3. **"One unit, one depth."** A survey that maps what exists and a dive into one thing it found
   are different units. Sharpest of the three, still not integrated.

A fourth, *name a job, not a category*, was worse than the hole. It would have forbidden the
survey, and a shallow survey is a legitimate unit: cheap, and it tells you which dive is worth
doing.

## Why none of them landed

Reading the skill whole. Rules 1 through 7 each do different work: test for oneness, placement,
anti-merge, scoping, gate response, cost admission, behaviour under pressure. Every candidate was
a second test for oneness sitting next to rule 1, doing rule 1's job through a different lens.

Three rewrites in three messages was the real signal. The specific instance was clear; the general
shape was not.

## Takeaways

- **An honest umbrella defeats the sentence test.** Width is invisible to a rule that only checks
  whether one sentence fits.
- **A bad patch is worse than an open hole.** *Name a job, not a category* would have banned
  reconnaissance, which is a unit worth having.
- **Churn is the signal to stop.** Three attempts meant the shape was unknown, not that the fourth
  would work.
- **A candidate rule is only judged in context.** Each version looked reasonable alone and was
  obviously redundant beside rules 1 through 7.
- **One incident does not generalise.** It earns an essay; a rule needs a pattern.

## Open questions

- **The hole is still open.** What closes it without forbidding legitimate wide-but-shallow units?
  Depth was the closest answer and it did not survive review.
- **Is survey-then-dive a real pattern**, or an artifact of this one probe?
- **Is `simplicity` already scope-drifted?** Rules 2 and 6 are placement and cost admission, not
  size. Both are useful; neither is "bound the size of a unit of work."
