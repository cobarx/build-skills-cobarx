# Simplicity is not size

**2026-09-20**

## Where we landed

`simplicity` led with "bound the size of a unit of work". That names the indicator, not the
principle. It now leads with **make every change cheap to understand**, and size is how you notice
when it is not.

No rules changed. The skill was already about cognitive load and was carrying the wrong headline.

## What went wrong

A probe script did five separable jobs: media stats, native text tracks, player method
enumeration, caption container discovery, fullscreen target resolution.

It passed rule 1. The sentence was *show what the browser exposes about a playing video*: true, no
"and", and it covers all five without strain. Rule 1's caveat about invented abstractions does not
fire either, because that sentence was not stretched to fit. It is simply accurate, and the
umbrella is genuinely that wide.

## Three failed patches

1. **"Bounded is not minimal."** Symptom, not action.
2. **"Count the jobs, not the sentence."** Correct, and rejected for the wrong reason.
3. **"One unit, one depth."** Survey and dive are different units. Closest, still bolted on.

A fourth, *name a job, not a category*, would have banned reconnaissance, which is a legitimate
unit. Worse than the hole.

## The actual diagnosis

Every patch tried to repair rule 1. Rule 1 was not broken. It is a **cheap proxy** for how much a
reviewer must hold, and a proxy can always be gamed by a wide enough umbrella.

With the headline wrong, rule 1 was the operative test and its gap was fatal. With the headline
right, rule 1 is one heuristic serving a stated principle, and the principle catches the probe on
its own: five integrations is five things to hold, whatever sentence covers them.

Which makes attempt 2 premature rather than wrong. Counting what must be held *is* the real
question; rule 1 is its shortcut. It was rejected as a redundant test for oneness because the
skill claimed to be about size.

## Takeaways

- **A heuristic cannot carry a principle the skill never states.** Name the goal, and the
  heuristics become servants rather than definitions.
- **When a rule keeps needing patches, check the headline.** Three rewrites in three messages was
  the signal, and none of them was the problem.
- **A bad patch is worse than an open hole.** *Name a job, not a category* would have forbidden a
  useful unit.
- **Thresholds are diagnostics.** A long function is not wrong for being long; it is long because
  something upstream went wrong.
- **Cheeseburger. No Coke, Pepsi.** Hampton sent the [SNL Olympia sketch](https://www.youtube.com/watch?v=puJePACBoIo) as a comment on this
  session, which is fair: he asked one question and got the whole menu, repeatedly. I then turned
  the joke into a design principle about curated option sets, which is its own kind of proof.
- **The principle applies to the conversation, not just the code.** A message is a change too.
  Feedback, a short answer, a diff. Writing at length is cheap for the author and expensive for
  the reader, which is the exact asymmetry this skill exists to correct. Every revision above was
  delivered as an essay when it should have been a paragraph and a patch.

## Open questions

- **Is survey-then-dive a real pattern**, or an artifact of one probe? Survey first is cheap and
  tells you which dive is worth doing, but that is one data point.
