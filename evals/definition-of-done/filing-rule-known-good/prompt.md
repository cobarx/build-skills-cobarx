---
name: filing-rule-known-good
description: Control. The agent repeats a known-good PR description verbatim, and every scored grader must pass it. See README.md.
tags: [control]
allowed_tools: []
---

Reply with exactly the text between the two lines of dashes, and nothing else. Don't add to it,
correct it or comment on it.

----------
## In one sentence

`durable-context` gains rule 6: a bug, gap, or risk you notice goes in the tracker by default, unless the dev has declared that area not-expected-to-work-yet.

## The rule

> 6. **A problem you notice is filed, not just mentioned.** A bug, gap, or risk spotted on the way to
>    something else goes in the tracker before the work moves on; said only in a chat, it is gone
>    when the chat ends. Unsettled severity or an unknown fix is no reason to wait: say so in the
>    issue, which is where that discussion belongs. The one exception is the developer's to make,
>    never yours to infer: early in a project, areas not expected to work yet can be declared, at the
>    entry point or in the moment, and problems there go unfiled.

The description also gains "when you notice a bug, gap, or risk, whether or not it is the task at hand", so the skill loads when it's needed and not only when something is being recorded.

## Commits

| Commit | What |
|---|---|
| `durable-context: a problem you notice is filed…` | The rule and the description trigger |
| `Decision 0011` (was 0010) | The three options (ask first; file and let the agent judge; file and let the dev declare exceptions) and why the third |
| `Bump to 0.12.0`, then 0.14.0 after #46 and #48 took 0.12.0 and 0.13.0 | Minor: a rule is added (`skill-versioning`) |

## Example

Rule 6 applied to a problem noticed while working on #94. It wasn't part of that task, so under the rule it goes in the tracker before the work moves on, without asking first:

> **Title:** #61 and #76 both bump the library to 0.17.0
>
> Both open PRs set `.claude-plugin/plugin.json` to `"version": "0.17.0"` (checked with `git show origin/<branch>:.claude-plugin/plugin.json` on each). Whichever merges second will merge that line silently, as happened with 0.12.0 and 0.13.0 on #44, and ship a second, different 0.17.0.
>
> **Severity and fix are open.** One of them should take 0.18.0 at merge (`skill-versioning` rule 5: a version only rises), but which depends on merge order, and that's for the owner.

The exception doesn't apply: nothing in this repo declares versioning an area not expected to work yet. Had the dev declared it, this would go unfiled, and the description would say so.

## Where it came from

A pubnet-tools session on 2026-09-24 found four real problems while doing other work, listed them in chat, and asked "should I open issues?". The dev's call: filing is the default. The only qualifier is early development, where issues for things not expected to work yet are noise, and that qualifier is the dev's to declare.

## Checks

- `wc -l skills/durable-context/SKILL.md`: 48, under the seventy-line limit (0009).
- Rule 6 is appended, not inserted, so no existing rule number moves.
- No new skill, no rename: minor, not major.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
----------
