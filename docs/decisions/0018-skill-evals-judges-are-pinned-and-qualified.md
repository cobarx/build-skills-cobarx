# 0018. `skill-evals`: a judge is a pinned model, approved by a repeatable qualification

- **Status:** Accepted
- **Decided:** 2026-10-05 · **Recorded:** 2026-10-04, revised 2026-10-05 · Claude Opus 5.5
- **Affects:** `skill-evals` (planned), which carries the rule to every eval suite under `evals/`

## Context

`claude plugin eval` judges `llm` graders with Haiku unless `--judge-model` says otherwise. On #61's
first case (a private project's clip, since replaced by the signups chart), Haiku passed both
controls, but on real replies it erred both ways. It failed a description containing "[Attach the
generated clip…]", which the grader explicitly accepts, and it passed a description that never asked
for the clip. Sonnet, rerun on the same commit, matched the author's reading of all six
descriptions, at $0.87 for the case against Haiku's $0.69.

The first version of this record settled on `--judge-model sonnet`. The owner's review
(2026-10-05): it "ties this to anthropic models and relies on behaviors for the current models
without reference to new versions of the same model being released." `sonnet` is an alias, so a
new release changes the judge without anyone seeing it, and #61's result files record only
`"sonnet"`, so which model was found good is not known. Then: "qualifying a model should be a
repeatable process. imo, a passing result is evidence attached to the decision to approve that
model."

Checked 2026-10-05 with Claude Code 2.1.289, on #61's known-bad control:

- `--judge-model claude-sonnet-5-5` runs, and the result file records that ID.
- A model that does not exist makes every grader throw ("judge call failed: There's an issue with
  the selected model"). The known-bad control still scores 0, as it expects; only the known-good
  control, falling from 1.0, shows the judge is gone.

## Options

- **An alias** (`sonnet`, as first decided). New releases arrive with no work, and unseen.
- **A pinned model, qualified by hand,** as #61 did: reruns, then a person reads the replies. It
  depends on who does it, and leaves nothing to attach but prose.
- **A pinned model, qualified by a fixed procedure,** each approval recorded with its result.

## Decision

A judge is a model pinned by its full ID (`--judge-model claude-sonnet-5-5`), never an alias, and
only a model that has passed qualification. A new version of an approved model is an unapproved
model. The rule names no vendor.

Qualification is the same steps every time:

1. **The controls behave.** Under the candidate, every LLM-graded case's known-bad control scores
   0 and its known-good control 1.0 (0017).
2. **It agrees with a person on real replies.** A fixed set of replies captured from real runs,
   each labelled PASS or FAIL per grader by a person before any candidate judges it, is graded by
   the candidate. It passes only if it matches every label.

Each approval is its own decision record, naming the model ID and the commit qualified at, with
the passing result (the runner's result file and report) committed beside it and linked.

## Consequences

- No judge is approved yet. #61's Sonnet runs are evidence for an alias, not for a pinned model.
  The first candidate is `claude-sonnet-5-5`.
- Follow-up, its own PR after #61: the qualification itself. That is the labelled set, captured
  from #61's replies (`fixtures` governs the capture), and one command that runs both steps and
  writes the result.
- Moving a pin is a new approval record. A retired model fails loudly, and the known-good control
  catches it.
- The runner is Claude Code's, so its judges are Claude models today; whether it accepts another
  vendor's is untested. The procedure does not depend on the vendor.
- Matching every label is strict. If a labelled set grows large enough that one disagreement is
  noise, the threshold is a new record.
