# decision-record-known-good

A control for `../decision-record-pr-description/`: its grader must pass a known-good description.

## Purpose

A grader is trusted only once it has been seen to fail a bad description and pass a good one. Its
partner is `../decision-record-known-bad/`. A result from the case counts only when both controls
behave (decision 0017).

The description is real: #52's description after the owner asked for an example. It adds `review`
rule 1 with the Nelson footnote applied: the raw Markdown, the same rendered live in the
description, and the file's line count under the new rule, measured beside the expected value.

## How it behaves

`claude plugin eval` starts an agent with no tools (`allowed_tools: []`), so it can't load a skill
that might rewrite the text, and sends `prompt.md`, which tells it to repeat the description
verbatim. The file in `graders/` is a symlink to the case's grader, so the two can't drift apart.
The case's `skill-fired` isn't included, because there's no run to inspect.

**Expected result: a score of 1.0, with and without the skills.** Any FAIL means the grader is too
strict to trust. Fix it, then rerun both controls before reading a result from the case. Also read
the reply in the report: if the agent didn't repeat the text verbatim, the run tested something
else.

```
claude plugin eval . --case decision-record-known-good --judge-model sonnet
```

## When to update

- **The case's grader changes.** Rerun this control and its partner.
