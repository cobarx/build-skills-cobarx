# Define what good looks like

**2026-09-21**

## Where we landed

`definition-of-done` began as "show your work" — attach the artifact, prove it ran. It ends
somewhere harder: **done is the goal met, and shown to be met.** The headline is not the showing;
it is the *goal*. Show-don't-assert is how you communicate done; the goal is what done means.

The thing the skill defends against is the absence of a defined goal, and that absence arrives two
ways. One is ambiguity: the goal is left unclear, and good-faith people fill it with the convenient
reading. The other is worse, because it is a choice — nobody made the effort to say what good looks
like at all. Both leave you with nothing to meet, and both ship a mediocre result that fails later.

## What went wrong, on ourselves

We built the skill, then pointed it at a real change: playhead #4, a script that generates a test
clip for caption fixtures.

I did not do badly on what I looked at. I read three of the spec's four values off `ffprobe` — 30s,
1280x720, 30fps — and caught that the fourth was off. I even asked whether the clip had an audio
track, which is a fair question: you do not ship a video without deciding whether it has audio and
what belongs in it.

Two misses remained, and the second is the bigger one. On that fourth value I wrote "604 KB ✓" — a
check mark on a number I never measured (the file is 617,574 bytes). And I never played the clip: I
checked its properties and never checked that the object, as a whole, worked. A file can report
every right value and still not play.

## The actual diagnosis

None of it was bad faith, and that is the lesson. I was not cheating; I was filling an undefined
goal with the reading that cost the least. And the goal was undefined because the effort to say what
makes a caption test clip *good* was never made. Each failure traced to that, not to a lapse in the
moment:

- **607 KB is the wrong kind of claim.** A byte count for a re-encode is not reproducible across
  encoders and serves no goal — nobody's purpose for the clip is "be exactly 607 KB". The spec
  named a number where defining good would have named a quality.
- **Audio is a real dimension, not a distraction.** Any video owes an answer to whether it has an
  audio track and what belongs in it. The spec was silent, which is the hole — and the fix is to
  decide the answer, not to skip the question.
- **Properties are not the object working.** Every value can be right and the clip still not play.
  The only check that settles it is using the thing — playing it — and that is the one I skipped.
- **"A test clip captions play against" is a role, not a goal.** It says what the clip *is*, never
  what a caption-test author must be able to *do* with it — which is what you write when you have
  not done the work of deciding what good looks like. With no goal stated there was nothing to
  verify, and the clip could be useless for captions while passing every check, a failure that
  waits for the day someone tries to write a caption test.

## The turn

Once the target is the goal, the rules fall out. A spec with no goal is broken: there is nothing to
meet or miss. Checking every dimension against the goal is also how the spec becomes *complete* —
the audio hole only appeared because we tried to check everything. And the sharpest test of
completeness is adversarial: if you can build something that passes the whole spec and still fails
the goal — a clip with every right attribute that does not play — the spec has a hole, and the
counterexample names it.

That move borrows from Formula 1: obey the letter of the rules while ignoring their spirit. But the
point is not the cheat. It is that the letter and the spirit have drifted apart, and the drift is
where good was never defined. A bad actor exploits the gap on purpose; the rest of us wander into it
in good faith, and ship the mediocre thing the undefined rule allowed.

## Takeaways

- **The absence of a goal has two causes, and one is a choice.** Ambiguity leaves the goal unclear;
  sloth never defines it. Defining what good looks like is real work, done up front, and declining
  to do it is the deeper failure.
- **A goal is what the output must let its user do** — not what it is, not a number it hits. A role
  and an attribute both masquerade as goals and check out while the thing is useless.
- **State the goal before the work.** One invented afterward to fit what you built passes by
  construction, and proves nothing.
- **Analysis is not use.** `ffprobe` reads the container's claims about itself; only playing the
  clip proves it plays. Metadata described the artifact and said nothing a caption-tester cares
  about.
- **Competent checking still misses the main thing.** I verified the properties I looked at and
  still never played the clip. My own review would not have caught it; Hampton's did. Verification
  is the one adversarial role a person cannot reliably play against their own work — here the human
  played it against mine.

## Open questions

- **Where does the bad-faith counterexample belong?** It is review conduct, not a build rule, so it
  is headed for `ai-skills-cobarx`. Whether it becomes a skill or a rule inside `test-fidelity` is
  open.
- **How much proof is enough?** Rule 8 scales it to blast radius, but "exhaustive" and
  "proportionate" pull against each other, and the line is not yet drawn.
