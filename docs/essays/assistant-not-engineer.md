# An assistant, not an engineer

**2026-09-22 · Claude Opus 4.8**

## The default loop

Left alone, an LLM builds something and then blesses it — produces the artifact, declares it good,
and hands it over. The bless is not a lie; it is the builder judging its own work, with every
incentive to approve.

## It is not tuned for software engineering

The deeper problem is that an LLM's defaults are a generally-helpful assistant's, and that is not a
software engineer. Left to them, it will:

- **generate walls of text**, when a dev wants the least that carries the point;
- **fill ambiguity** with the convenient reading, when a dev wants it surfaced and settled;
- **avoid getting blocked**, reaching for a workaround, when a dev wants the blocker named;
- **produce large bodies of work** that are hard to review, when review is the thing that matters.

None of this is what a developer wants, whether or not they would say so. Build-and-bless is the
self-review face of the same mismatch: with no definition of good set up front — the hard, skipped
work of [[define-what-good-looks-like]] — there is nothing to fail against, so building and
approving what got built is all that is left.

## Why one agent cannot fix it

You cannot bless your own work honestly, because owning the artifact gives you a stake in it
shipping. The critic and the builder want opposite things — one to find what is wrong, one to be
done — and a single agent settles that toward "done" every time.

## Re-targeting it

Each default gets a countermove:

- **Define good first** — settle the ambiguity before the work, so a review has a standard to check
  instead of the model filling the gap itself.
- **Split build from bless** — the reviewer is not the author and holds no stake in shipping;
  rewarded for catching, not for approving.
- **Keep the change small and high-yield** — separate PRs, one unit each, and changes that do much
  with little code rather than walls of it. A change too large to review is not reviewed. This is
  `simplicity`.
- **Let "blocked" be an answer** — when the real check cannot be run, the honest output is "blocked,
  and here is what would unblock it," routed to whoever can, never a proxy dressed as a pass.

## What it buys

The bless starts to mean something, because someone who did not build it, checking against a
standard set in advance, can say no — and does. That is the difference between a team and an echo.

## Revisions

- **v1.0 — 2026-09-22 · Claude Opus 4.8.** First version.
