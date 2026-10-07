# 0026. `simplicity` loads at session start

- **Status:** Accepted
- **Decided:** 2026-10-06 (#PR) · **Recorded:** 2026-10-06 · Claude Opus 5.5
- **Affects:** `simplicity`, how the plugin loads

## Context

`simplicity`'s description says it applies before starting any unit of work. In a pilot of 120
headless Claude Code sessions on MaintainBench requirement changes, it never loaded, and nor did
any other skill in the library: the model judged the tasks too small. Only the descriptions were in
context, and the library performed close to plain Claude Code. A 65-line CLAUDE.md that is always
in context (Karpathy's four principles) changed what the agent did.

## Options

- **Reword the description.** Portable to every agent, but the description already says "before
  starting any unit of work" and did not trigger.
- **Ship an always-loaded CLAUDE.md.** A Claude Code plugin cannot; a hook is how a plugin puts
  text in every session.
- **A `SessionStart` hook that injects a summary of the core rules.** A second copy of the rules
  that drifts from the skill.
- **A `SessionStart` hook that injects `simplicity` in full.** The skill is the copy.

## Decision

A `SessionStart` hook (`hooks/hooks.json`, `hooks/session-start`) injects `simplicity`'s body,
with its base directory so its reference resolves, on startup, `/clear` and compaction. Only
`simplicity`: it is the one skill that applies to every unit. The others still load when their
descriptions match.

## Consequences

- Every Claude Code session carries `simplicity`, about 60 lines, whether or not the task needs it.
- Agents that don't run Claude Code hooks (Codex, Copilot, Cursor, Gemini CLI) are unchanged; the
  README says to point their always-loaded instructions at the skill.
- A change in how a skill loads is a breaking change (`skill-versioning`); below 1.0 it takes the
  minor slot: 0.18.0 → 0.19.0.
