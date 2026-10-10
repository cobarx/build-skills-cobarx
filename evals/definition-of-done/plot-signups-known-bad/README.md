# plot-signups-known-bad

A control for `../plot-signups-pr-description/`: its graders must fail a bad description.

## Purpose

A grader that has only ever been seen to pass proves nothing, because it might pass anything.
This control shows that the case's four `llm` graders fail a description that's missing every part
of validation. Its partner, `../plot-signups-known-good/`, shows they pass a good one. A result from
the case counts only when both controls behave (decision 0017).

The description is synthetic, written for this control. It says what the script does and ends
"Tested locally, works.": no goal, no checks, no look at the chart, and no PNG.

## How it behaves

`claude plugin eval` starts a fresh Claude Code agent with no tools (`allowed_tools: []`), so it
can't load a skill that might rewrite the text. It sends `prompt.md`, which tells the agent to
repeat the description verbatim. It then grades the reply. The files in `graders/` are symlinks to
the case's graders, so the two can't drift apart. The case's two `tool_used` graders aren't
included, because there's no run to inspect.

**Expected result: a score of 0, with and without the skills.** Every grader FAILs, so the runner
exits with status 1. That's correct here. Any PASS means a grader too lenient to trust: fix it,
then rerun both controls before reading a result from the case. Also read the reply in the report.
If the agent didn't repeat the text verbatim, the run tested something else.

To run it, from the repo root:

```
claude plugin eval . --case plot-signups-known-bad --judge-model claude-sonnet-5-5
```

The first run in a checkout asks you to confirm you trust this plugin. When you run it yourself,
the runner publishes the HTML report to your claude.ai account; add `--no-publish` to keep it
local.

## When to update

- **Any `llm` grader of `plot-signups-pr-description` changes.** Rerun this control and the
  known-good one.
- **The change in the case's `files/` changes,** if this description no longer matches it.
