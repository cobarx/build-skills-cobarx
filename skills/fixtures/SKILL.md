---
name: fixtures
description: This skill should be used whenever a test needs data that originates outside the codebase: command output, network responses, sensor readings, third-party API payloads, page state from a site you do not control. It governs where that data comes from and what has to be recorded alongside it. Load it before writing a test that needs such data, before writing or running a capture, and when a fixture stops matching reality.
---

# fixtures

Test data comes from the real world, or says that it does not.

A fixture that was never real shares every blind spot of the code written beside it. It will agree
with your assumptions because it was made from them.

## Rules

1. **Prefer capture; label everything else.** Not from memory, not from a specification, not from
   a string typed until the test passed. Capture is sometimes impossible or impractical: the system
   does not exist yet, access is unavailable, the real thing is gigabytes, it needs a setup you
   cannot reproduce. Then derive from a capture where you can (trim, sample, redact) and mark what
   is synthetic. Synthetic data is also the right tool for extremes a real corpus will not reliably
   produce. **Unlabelled synthetic data is the failure, not synthetic data.**

2. **The capture script ships.** It lives in the repo and is run, not described. Anything captured
   by hand once will need capturing again, and by then the steps are gone.

3. **Verify preconditions, then record.** A capture environment can fail silently and produce data
   indistinguishable from real behaviour. Assert what must be true and write nothing otherwise.
   Saved, that fixture encodes your environment's failure as the system's behaviour, and it will
   look plausible forever.

4. **Record the conditions, not just the data.** Date, environment, and anything that changes what
   the source returns. A capture from a system you do not control is a dated snapshot, not a fact,
   and without the conditions a later capture cannot be diffed against it.

5. **Do not hardcode what can be derived.** Anything the source can tell you, take from the source.
   Operator-typed fields are the ones that go stale, and they go stale silently while every derived
   field stays correct.

6. **Scrub at capture, not at commit.** Secrets, tokens and personal data are removed by the
   capture script. A scrub step that runs later is a scrub step that gets skipped once.

7. **Defer a missing fixture; do not invent one.** Mark the test ignored, naming what is needed and
   where to get it. An ignored test is honest; a test passing against imagined data is not.

8. **Vendor only what you can license.** A corpus with unclear provenance is a liability sitting in
   the repository, whatever its technical merits.

## Not here

What a test asserts and where it sits are `test-fidelity`. When the test gets written is `tdd`.
This skill only governs where its data came from.

---

Decisions affecting this skill: `docs/decisions/*-fixtures-*.md`
