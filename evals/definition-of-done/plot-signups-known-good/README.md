# plot-signups-known-good

A control for `../plot-signups-pr-description/`: its graders must pass a good description.

## Purpose

A grader can be too strict as well as too lenient. One that fails good work makes the skill look
useless. This control shows that the case's four `llm` graders pass a description that covers every
part of validation. Its partner, `../plot-signups-known-bad/`, shows they fail a bad one. A result
from the case counts only when both controls behave (decision 0017).

The description is synthetic, written for this control from real measurements of the PNG the case's
script produces:

- the bar heights match `round(signups / 260 * 319)` exactly;
- the baseline sits at pixel row 339 of 360, and every bar stands on it.

It states the goal, lists the checks with expected and measured values, says what the chart showed
when looked at, tells the developer to attach the PNG, and names what wasn't checked.

## How it behaves

`claude plugin eval` starts a fresh Claude Code agent with no tools (`allowed_tools: []`), so it
can't load a skill that might rewrite the text. It sends `prompt.md`, which tells the agent to
repeat the description verbatim. It then grades the reply. The files in `graders/` are symlinks to
the case's graders, so the two can't drift apart. The case's two `tool_used` graders aren't
included, because there's no run to inspect.

**Expected result: a score of 1.0, with and without the skills.** Every grader PASSes. Any FAIL
means a grader too strict to trust: fix it, then rerun both controls before reading a result from
the case. Also read the reply in the report. If the agent didn't repeat the text verbatim, the run
tested something else.

To run it, from the repo root:

```
claude plugin eval . --case plot-signups-known-good --judge-model sonnet
```

The first run in a checkout asks you to confirm you trust this plugin. When you run it yourself,
the runner publishes the HTML report to your claude.ai account; add `--no-publish` to keep it
local.

## When to update

- **Any `llm` grader of `plot-signups-pr-description` changes.** Rerun this control and the
  known-bad one.
- **The change in the case's `files/` changes.** This description quotes its measurements, so
  remeasure and rewrite it.
