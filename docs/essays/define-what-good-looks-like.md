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
clip for caption fixtures. The skill should have made that review rigorous. Instead it was inert on
the exact case it was written for.

The PR's spec was four values: 30s, 1280x720, 30fps, 607 KB. I read three off `ffprobe` and, on the
fourth, wrote "604 KB ✓" — a check mark on a number I never measured. The file was 617,574 bytes.
Then I invented a dimension the spec never mentioned — does it have an audio track? — and chased
that, because it was easy, while the four stated claims sat unchecked.

A skill whose whole point is *show, don't assert* had let me assert. Twice.

## The actual diagnosis

None of it was bad faith, and that is the lesson. I was not cheating; I was filling an undefined
goal with the reading that cost the least. And the goal was undefined because the effort to say what
makes a caption test clip *good* was never made. Each failure traced to that, not to a lapse in the
moment:

- **607 KB is the wrong kind of claim.** A byte count for a re-encode is not reproducible across
  encoders and serves no goal — nobody's purpose for the clip is "be exactly 607 KB". The spec
  named a number where defining good would have named a quality.
- **Audio was not in scope, and dropping it silently was also wrong.** A dimension the spec never
  named is a hole in the spec, found by checking exhaustively — not something to chase, and not
  something to bury. State it, and let the goal decide.
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
- **A skill can be inert.** This one failed its own worked example, live, and only Hampton's refusal
  to let "604 KB ✓" stand drove the fixes. Verification is the one adversarial role a person cannot
  reliably play against their own work — here the human played it against mine.

## Open questions

- **Where does the bad-faith counterexample belong?** It is review conduct, not a build rule, so it
  is headed for `ai-skills-cobarx`. Whether it becomes a skill or a rule inside `test-fidelity` is
  open.
- **How much proof is enough?** Rule 8 scales it to blast radius, but "exhaustive" and
  "proportionate" pull against each other, and the line is not yet drawn.
