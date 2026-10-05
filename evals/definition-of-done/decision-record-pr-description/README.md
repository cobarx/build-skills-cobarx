# decision-record-pr-description

An eval case for the `definition-of-done` skill.

## Purpose

This case answers one question. When an agent writes the PR description for a change whose output
is a rule (a decision record, a convention), does `definition-of-done` make the description show
the rule applied to a real case, where the description without it only restates the rule?

A script's output is easy to recognise: run it and there is a file. A decision's output is the work
it governs, which no command produces. The failure is real: #52, this repo's decision 0013 (cite
sources in footnotes), was described with no footnote shown until the owner asked for an example.

**The change is a snapshot,** not synthetic: `files/` holds #52's files at commit `2067919` (the
new decision, the files it updates, and two skills it names as cases). The controls are #52's own
descriptions, before and after the example was added.

## How it behaves

`claude plugin eval` (Claude Code's eval runner) runs this case, set up by `case.yaml`:

1. With `--scaffold`, it runs `setup.sh`, which copies `files/` into the agent's empty workspace.
2. It starts a fresh agent, the **agent under test**, with this repo's skills installed, and the
   tools `Skill`, `Bash`, `Read`, `Glob` and `Grep` (Bash only with `--allow-tools Bash`), so it
   can measure what it shows, such as a file's line count. It runs in a sandbox where this repo and
   its graders aren't visible, capped at 25 turns and 600 seconds.
3. It sends the prompt from `case.yaml`: a request for a PR description, with no mention of
   examples, testing or evidence.
4. It grades the final reply with each file in `graders/`, 5 times, then 5 more with the skills
   not installed.

| Grader | Checks | Counts toward the score |
|---|---|---|
| `skill-fired.md` | The agent loaded `definition-of-done` (a symlink to the plot case's grader). | No. Reported separately, for the runs with skills only. |
| `shows-the-decision-applied.md` | An excerpt of a real file with the decision applied, footnote reference and definition both shown. | Yes |

The `llm` grader is judged by Sonnet (decision 0018). Read a sample of the replies too (decision
0017). A result counts only when `../decision-record-known-bad/` scores 0 and
`../decision-record-known-good/` scores 1.0.

To run the case and both controls, from the repo root:

```
claude plugin eval . --case 'decision-record-*' --scaffold --allow-tools Bash --judge-model sonnet
```

The command exits with status 1 because the known-bad control scores 0, which is what it should
do. The flags, including the `~/.ssh` limit on granting Bash, behave as in
`../plot-signups-pr-description/README.md`.

## When to update

- **The skill's `description` changes.** Rerun, and confirm `skill-fired` still passes.
- **The grader changes.** Rerun both controls.
- **A new Claude model ships.** Rerun: the description without the skill may change.
- **Decision 0013 is superseded.** The snapshot still works as a case; it needn't follow `main`.
