# plot-signups-pr-description

An eval case for the `definition-of-done` skill.

## Purpose

This case answers one question. When an agent writes the PR description for a finished change,
does having `definition-of-done` installed make the description validate the change, where the
agent's description without it doesn't?

"Validate" means four parts:

1. **Critical elements.** What must be true for the change to work, each one checked.
2. **Sanity checks.** Look at the output and judge whether it's in the ballpark of what you
   expected. That catches what properties never show: corruption, a bad render, something drawn
   wrong.
3. **How it was tested, and the results.** Observed values beside expected ones, not the word
   "tested".
4. **The input provided.** Here that's the PNG, attached to the PR, so another person or agent can
   follow the same steps. The agent can't upload, so it passes by telling the developer to attach
   the file; a relative embed (which doesn't render in a PR) or an unbacked "is attached" doesn't.

The failure modes come from a real one, in playhead, a private project of Hampton's: the first PR
description for a script that generated a test video clip, written without this skill. It read
metadata instead of looking at the output, checked one point, stated a value it hadn't measured,
gave no goal, and attached nothing.

**The change is synthetic,** written for this eval (`fixtures` rule 2). `files/` holds a small
script that draws a bar chart of monthly signups as a PNG, using only Python's standard library,
and its data. The change works: the chart is correct (measured: all 12 bars the right height,
standing on the baseline). So the question is how the agent shows that, not whether it finds a
bug. A broken version of the same change, where the question is whether the agent stops calling
it done, belongs to a separate case.

Two graders tell an agent that looked from one that read only properties. `looked-at-the-chart`
records from the run whether the agent opened the PNG. `sanity-checks` asks it to say what it saw,
which a properties-only check can't.

The answer is only as good as the graders. Two controls check them: `../plot-signups-known-bad/`
(they must fail a bad description) and `../plot-signups-known-good/` (they must pass a good one).
Run both before trusting a result here, and read a sample of the replies too (decision 0017).

## How it behaves

`claude plugin eval` (Claude Code's eval runner) runs this case, set up by `case.yaml`:

1. It runs `setup.sh` in the agent's empty workspace (only when given `--scaffold`). That copies
   `files/` in and runs the script once, as the developer in the prompt says they did, leaving
   `signups.png` there.
2. It starts a fresh Claude Code agent, the **agent under test**, with this repo's skills
   installed. Its tools are `Skill`, `Bash`, `Read`, `Glob` and `Grep`, so it can run the script,
   inspect files and look at the PNG. Bash is only granted when the command passes
   `--allow-tools Bash`. The agent runs in a sandbox whose home is a temporary directory, so it
   can't read this repo or its graders. Each run is capped at 25 turns and 600 seconds.
3. It sends `execution.prompt` from `case.yaml` as the agent's first message: a request for a PR
   description, with no mention of testing.
4. It grades the agent's final reply with each file in `graders/`.
5. It does this 5 times (`runs: 5`), then 5 more times with the skills not installed.

| Grader | Checks | Counts toward the score |
|---|---|---|
| `skill-fired.md` | The agent called `Skill` to load `definition-of-done`. | No. Reported separately, for the runs with skills only. |
| `looked-at-the-chart.md` | The agent opened a PNG with `Read`, which is how it sees an image. A fact from the run's record. | Yes |
| `critical-elements.md` | Part 1 | Yes |
| `sanity-checks.md` | Part 2: the reply says what the chart showed, against what the data should look like | Yes |
| `how-tested-and-results.md` | Part 3: observed beside expected. Empty slots fail. | Yes |
| `input-to-repeat.md` | Part 4: tells the developer to attach the PNG to the PR | Yes |

The `llm` graders are judged by the pinned model `claude-sonnet-5-5`, voting three times; the
majority decides. Under decision 0018 a judge must be approved by qualification first, and none is
yet (#99), so results from this case are provisional until then.

**Why five runs.** The agent samples its reply, so the same prompt gives different replies. Five
runs per arm show a consistent difference (for example 5/5 against 0/5) more reliably than the
runner's default of three, at about two-thirds more cost. They still can't measure a small effect.

**Reading the result.** The runner reports a score with the skills, a score without, and the
difference. A positive difference means the skill made the description validate the change more
fully. If the runs without the skills already score full marks, the case no longer separates them,
so treat that as a broken case, not a pass.

To run the case and both controls in one command, from the repo root:

```
claude plugin eval . --case 'plot-signups-*' --scaffold --allow-tools Bash --judge-model claude-sonnet-5-5
```

Read the three result lines. The result counts when `plot-signups-known-bad` scores 0 and
`plot-signups-known-good` scores 1.0; then `plot-signups-pr-description`'s line is the answer. The
command exits with status 1 because the known-bad control scores 0, which is what it should do.
To run the case alone, use `--case plot-signups-pr-description` with the same flags.

- **`--scaffold`** runs `setup.sh` as you. It only copies files into the agent's workspace and runs
  the script there.
- **`--allow-tools Bash`** grants the agent a shell, inside the runner's sandbox. The runner
  refuses to grant one if your `~/.ssh` contains a symlink, because the sandbox can't then
  reliably keep the agent out of it.
- **The first run in a checkout** asks you to confirm you trust this plugin.
- **The HTML report:** when you run it yourself, the runner publishes it to your claude.ai account;
  add `--no-publish` to keep it local. A run started by Claude Code keeps it local.

## When to update

- **The skill's `description` changes.** That text decides whether Claude loads the skill. Rerun,
  and confirm `skill-fired` still passes.
- **The four parts of validation change.** The scored graders encode them. Rerun both controls
  after any grader change.
- **A new Claude model ships.** Rerun: the description without the skill may get better or worse,
  which moves the difference.
- **The judge's pin moves.** A new judge is approved by its own decision record (0018). Change
  `--judge-model` in all three READMEs, then rerun both controls and the case.
- **The change in `files/` changes.** The `sanity-checks` grader and the known-good control both
  describe what the chart shows. Keep the three in step, and look at the new PNG yourself.
