# Define what good looks like

**2026-09-21**

## Where we landed

`definition-of-done` began as "show your work" and ended somewhere harder: **done is the goal met,
and shown to be met.** The skill defends against the *absence* of a goal, which arrives two ways —
ambiguity, where the goal is left unclear and filled with the convenient reading, and, more often,
the goal never set at all — because defining what good looks like is hard, unglamorous work that
takes experience to do. Both leave nothing to meet, and both ship a mediocre result that fails
later.

## What the clip taught

We dogfooded the skill on playhead #4, a script that generates a test clip for caption fixtures —
and it caught me out. I checked three of the spec's four values off `ffprobe` competently enough
(30s, 1280x720, 30fps). Three things I did not do, in ascending order of how much they mattered:

- I wrote "604 KB ✓" on the fourth value without measuring it (it was 617,574 bytes). *Show, don't
  assert* — even to yourself.
- I never played the clip. Properties are not the object working; a file can report every right
  value and still not play.
- No one asked the only question that mattered: **is the clip useful for testing captions?** It can
  hit every property, play cleanly, and still be useless for its one job — captions illegible over
  the busy pattern, nowhere defined for them to land. That is the goal, and it went unexamined.

The through-line: a goal is what the output must let its *user do* — not what it is, not a number it
hits, not even that it runs. State it before the work, or a goal fitted afterward to what you built
passes by construction. And a spec you can satisfy while still missing the goal has a hole — a
dimension it never named (the clip's audio), or a bar it never set. The way to find the hole is to
try to slip through it.

## What I'll carry

- **The hardest part is defining good, which is why it gets skipped.** It is unglamorous, and it
  takes experience to know what good even looks like — so people and agents alike quietly leave it
  undone. More mediocrity traces to a goal never set than to a job done badly.
- When the rules leave room — a loophole, an ambiguity — you get unintended results, in good faith,
  no villain required.
- Verification is the one adversarial role you cannot reliably play against your own work. I
  verified competently and still missed the main thing; Hampton's review caught it, not mine.

## Open question

How much proof is enough? The skill scales it to blast radius, but "exhaustive" and "proportionate"
pull against each other, and the line is not yet drawn.
