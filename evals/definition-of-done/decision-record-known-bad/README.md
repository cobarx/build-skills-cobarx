# decision-record-known-bad

A control for `../decision-record-pr-description/`: its grader must fail a known-bad description.

## Purpose

A grader is trusted only once it has been seen to fail a bad description and pass a good one. Its
partner is `../decision-record-known-good/`. A result from the case counts only when both controls
behave (decision 0017).

The description is real: #52's description as first posted. It summarises the decision well, names
its sources, and reports a rendering check ("I ran the decision's example through GitHub's Markdown
API"), but shows no file with the decision applied. That makes it a hard control: a lenient grader
would take the check's report for the example.

## How it behaves

`claude plugin eval` starts an agent with no tools (`allowed_tools: []`), so it can't load a skill
that might rewrite the text, and sends `prompt.md`, which tells it to repeat the description
verbatim. The file in `graders/` is a symlink to the case's grader, so the two can't drift apart.
The case's `skill-fired` isn't included, because there's no run to inspect.

**Expected result: a score of 0, with and without the skills.** Any PASS means the grader is too
lenient to trust. Fix it, then rerun both controls before reading a result from the case. Also read
the reply in the report: if the agent didn't repeat the text verbatim, the run tested something
else.

```
claude plugin eval . --case decision-record-known-bad --judge-model sonnet
```

## When to update

- **The case's grader changes.** Rerun this control and its partner.
