# 0013. `spec` triggers on observable events, and builds the goal with its owner

- **Status:** Accepted
- **Decided:** 2026-10-03 · **Recorded:** 2026-10-03 · Claude Opus 5.5
- **Affects:** `spec`

## Context

In a CampaignStop session (sorting unsolicited texts on Android), an agent went from a first
observation to a policy four times without loading `spec`. It suggested keywords before seeing a
text, called `End2End` "a good marker" from a sample that keyword had helped select, and gave the
marker a 95% confidence without measuring it. It also proposed a category table and an LLM
architecture before the goal was set. `spec` was installed and listed throughout. The owner's
diagnosis: the problem was solved without clarifying the goal, abstracting it into the general
problem, and then specifying it.

Against the session record, the skills that fired had concrete triggers: `fixtures` on test data,
`skill-versioning` on `plugin.json`, `simplicity` on a repo instruction. The diagnosis drawn from
that record was three gaps in `spec`:

- **A self-diagnosing condition.** "When work jumps to a solution before what it must do is
  written down" fires only if the agent notices it is jumping, which is the blind spot.
- **"A change" scopes it to code.** Every jump happened while answering, recommending, or
  comparing in conversation, which did not read as a change.
- **It assumed a goal exists.** "No goal, no spec" names the gap but not the act that closes it:
  asking the owner. Nothing covered abstracting the instance into the general problem.

A headless check then tested the first two gaps (fresh session per run, only this plugin, Skill
the only tool, 3 runs per cell, Opus 5.5):

| Prompt from the session | main | this change |
|---|---|---|
| "Would it be possible to create an app that…" | 0/3 | 3/3 |
| "…a local LLM or a pattern match. Which should we use?" | 3/3 | 3/3 |
| "Let's start a new project for…" | 3/3 | 3/3 |
| "What does the -n flag do in grep?" (control) | 0/3 | 0/3 |

So the old triggers missed feasibility questions, but they already caught a choice handed over in
a fresh session. In the CampaignStop session the choice came late in a long conversation, and
`spec` still did not load. That is a session-depth effect this check does not reproduce, and the
change does not claim to fix it.

The owner then added a requirement: they explore and clarify rather than know the goal up front,
and the skill should support building the goal over time. As written, `spec` worked against that:
"state it before the work" treated any later change to the goal as suspect, and "what before how"
read as "do not explore until the goal is settled".

## Options

- **Leave the triggers and add rules.** The rules would still not load for a feasibility question
  (0/3 on main).
- **Make `spec` always-on through CLAUDE.md.** Reaches only repos whose CLAUDE.md says so, and
  costs context in every session.
- **Observable triggers plus rules.** Triggers name events the agent can see: being asked
  whether or how, being about to recommend or compare, being handed options, starting a project.

## Decision

Observable triggers, and three rules:

- *The goal comes from its owner, often in pieces.* Ask what the next step depends on, and don't
  hold the work for a full answer.
- *Keep a working goal where both can see it.* A dated draft with open questions beside it. When
  it moves, recheck what rested on the earlier draft. A product goal holds while its features go
  through discovery (the owner's framing: "standard product design", with the product goal "build
  an app that allows people to not deal with unwanted political texts" and categorizing as the
  first feature in discovery). Product, feature and discovery are industry terms, per 0006. The
  owner first said R&D; discovery is the product-design term for ideation and research before a
  feature is built, paired with delivery (Cagan, *Inspired*; Torres, *Continuous Discovery
  Habits*).
- *Specify the class, not the instance.*

Rule 1 covers a how-question that arrives without its what, and separates exploring to find the
what from choosing the how. The goal rule now separates a goal refined by what was learned (the
process working) from one fitted to what was built (the failure it always guarded against).

Understanding the problem, gathering data, and finding patterns before the goal is set stay out of
`spec`. They belong to the planned *why* skill, which this session gives its second instance.

## Consequences

- `spec` loads for feasibility questions as well as choices and new projects, and not for an
  unrelated question (table above). Three runs per cell bounds this loosely; it is a check, not a
  rate.
- Whether `spec` loads deep in a long session is untested and is the failure that started this.
  It needs a check that replays a long conversation before the prompt, or an always-on rule;
  the test and the decision it feeds are #58.
- Wider triggers cost context in more sessions; if `spec` fires where it adds nothing, narrow the
  triggers in a new record.
- Changing how a skill is loaded is a breaking change; below 1.0 it takes the minor slot.
