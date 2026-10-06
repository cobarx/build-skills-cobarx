# Best practices without the campaign

**2026-10-05 · Claude Opus 5.5**

When an agent does the work, a best practice is something it loads as the work starts, not
something reviewers enforce after. That removes most of what a practice cost. Cost was never the
main reason practices went unwritten, though: most developers aren't in the habit of setting them.
This essay covers what a practice used to cost, what replaced that, how the habit can move into
the process, and what is still left to do.

## What a best practice used to cost

- **The experience to identify it.** A best practice is a general rule, and a general rule takes
  exposure to many problems: enough failures to see what can go wrong, and which practice would
  have prevented each one. One bad incident teaches a fix. A rule takes years of them.
- **Circulating it.** It goes in a wiki, a talk, or an onboarding doc, and every new hire has to
  find it.
- **Getting buy-in.** Everyone who would follow it has to agree to, or at least not resist.
- **Enforcing it in review.** Someone checks every PR against it and leaves the same comment for
  the tenth time.
- **Getting people used to feedback.** People take a correction better the more often they've
  had one. Until then, each correction costs some goodwill.

Enforcement costs recur. They are paid on every PR, for every person, and again whenever someone
joins. A team that did set practices enforced the ones a reviewer would notice and let the rest
decay into a wiki page nobody opened.

Most teams never got that far, and not because they weighed the cost and declined. Setting
practices isn't something most developers do as a habit. A choice gets made in a PR, works, and
gets copied, and nobody stops to ask whether it should be the rule.

## What replaced it

An agent loads the practice at the start of a unit of work and follows it while it works. In this
repo that is the first line of AGENTS.md: load `simplicity` before starting any unit of work. The
agent doesn't need persuading, doesn't resent the tenth correction, and doesn't forget the rule
between tasks. Circulation and getting used to feedback drop to nearly nothing, and buy-in is paid
once.

Because the practice is part of the process, the check before merging becomes a final
verification pass and stops being the main defence. Deming's third point asks for exactly this:
"Cease dependence on inspection to achieve quality," by "building quality into the product in the
first place."[^deming] The check still runs. Its job is to confirm that the process produced what
it was supposed to, not to find out for the first time whether it did. A failed check is
therefore news about the process: a rule that didn't load, or a rule that said the wrong thing.
The fix goes into the skill, not the PR.

## Finding and writing the rule got cheaper too

The work that remains is mostly finding the practice and writing the rule, and that is no harder
than it was. Usually it is easier, because the agent does much of the work:

- **Experience.** It has seen far more failures than any one developer: other codebases,
  postmortems, and the literature that generalised them. It can name what tends to go wrong and
  the practice that prevents it, without the team living through each failure first.
- **Research.** It finds the standard, the prior art and the sources, so the rule can cite them
  rather than restate them. [Quality is defined by the customer][tqm] was researched this way.
- **Drafting.** It writes a reasonable first version of the rule from a sentence of intent.
- **Alignment.** It searches the existing rules for any that conflict and brings them in line,
  which used to depend on someone happening to remember the old rule.

The author's job moves from researching, writing and campaigning to deciding: whether the draft is
the rule they mean, and whether to adopt it.

## The habit can live in the process

Cheaper practices don't create the habit of setting them. What can is making it a step of the
process, triggered when the moment comes rather than left to someone remembering. Some skills
here do this already. `decision-log` triggers when a choice is made between options, so the
choice gets recorded rather than copied. `adopting-standards` triggers before a format or
convention is invented, so the agent looks for a settled practice first. The developer doesn't
need the habit, because the agent has the trigger.

## What is still left

**The rule has to be right.** An agent follows a wrong rule as reliably as a right one, so a bad
practice now spreads as cheaply as a good one. Deciding is the step that stays human. The agent
can help, though: it can evaluate a proposed rule and find examples that test whether the pattern
really generalises. If asked, it can also push back on the author's least-informed impulses
before they become rules.

**The rule has to say what it means.** A person reading a vague rule fills it in from shared
context. An agent follows the words as written. That is why the test for every line here is
whether it changes what anyone does ([The outline is the skill][outline]). The same evaluation
covers this: an agent can say where a rule is ambiguous before it's adopted.

**Some rules need a judge.** A linter checks layout and thresholds. Whether a name fits, or a
unit's purpose fits one sentence, needs a model to judge. That judge then has to be qualified and
pinned like any other dependency ([0018][0018], [0024][0024]).

**Buy-in, once.** Code a person writes by hand goes through the same agent review, and that review
requires it to conform to the practice. The team still has to agree to the rule. After that, the
agent leaves the feedback, which is consistent and impersonal, so few people argue with it. No
reviewer has to keep enforcing the rule and no goodwill gets spent, so the social cost is paid
once, when the rule is adopted, not on every PR.

## A workshop with a place for everything

A collection of well-written practices makes for a more pleasant place to work. Compare a
cluttered workshop with one where each tool has its place and each job has its workstation. In the
cluttered one, every job starts by searching for the tool and making again a decision someone
already made, because it was never put away where the next person could find it. In the
organised one, you reach for the tool and start work. Settled practices do this for a codebase:
the routine questions are already answered, so attention goes to the work that is actually new.
Deming's twelfth point asks for this, removing the barriers that rob people of their "right to
pride of workmanship."[^deming]

## What it shapes

- **Trigger on the moment a practice is needed.** A skill that loads when a choice is made does
  the work of a habit nobody had to form.
- **Write down the practices you believe in.** The cost of keeping one is mostly gone. A practice
  that was never worth a campaign is worth a skill.
- **Treat a failed final check as a defect in the process.** Fix the skill that should have
  prevented it, not only the change it caught.
- **Spend review on the rules, not on compliance.** The judgment people used to spend repeating
  comments goes into deciding whether a rule is right.

## Notes

The observation is Hampton's, on 2026-10-05: the effort of documenting best practices,
circulating them and getting buy-in "all goes away when you can validate at the end and specify
that the best practices are part of the development flow."

## Revisions

- **v1.0 · 2026-10-05 · Claude Opus 5.5.** First version.

[tqm]: quality-is-defined-by-the-customer.md
[outline]: outline-is-the-skill.md
[0018]: ../decisions/0018-skill-evals-judges-are-pinned-and-qualified.md
[0024]: ../decisions/0024-skill-evals-a-judge-is-pinned-by-its-model-alone.md

[^deming]: W. Edwards Deming, *Out of the Crisis* (MIT Press), pp. 23-24, as condensed by the
    W. Edwards Deming Institute, "Dr. Deming's 14 Points for Management",
    <https://deming.org/explore/fourteen-points/>.
