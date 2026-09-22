---
name: durable-context
description: This skill should be used when recording a decision, a follow-up, project knowledge, or working state; when tempted to leave it in agent memory, a chat, or a PR description; or when deciding where a note should live so the next person or agent can find it. It governs where context lives, not what any single document says.
---

# durable-context

Context lives in the project, where the next reader, human or agent, will find it.

Context kept in a private store, a chat, or a soon-buried PR description is context no one can find
later. If it matters past this moment, it belongs in the project, in the open.

## Rules

1. **Project context goes in the project, not in private memory or a chat.** Decisions, knowledge,
   and state that others will need live in a repo file or an issue, readable by humans and agents
   alike. A private note about how you yourself operate is the exception, and the only one.

2. **Deferred work is an issue or a tracked file, never a PR description.** A PR body is read once
   and buried; a follow-up has to outlive it.

3. **Index every context file so a reader can reach it from the entry point.** Follow the indexes
   down from the `README` or `CLAUDE.md`; in a nested project a file's link lives in the nearest
   index, not the root, and each index points on to the next. A file no chain of indexes reaches
   cannot be found, which is the same as not existing.

4. **Keep it plain and open.** Markdown or the like, readable without a particular tool. If only one
   tool can read it, it is hidden.

5. **One home per kind.** Decisions to `decision-log`, open questions to `docs/context`, rationale
   to `essays`, so a reader knows where to look before they look.

## Not here

The *form* of a decision record is `decision-log`. Writing a good README or laying out a project is
`organize`. This governs *where* context lives and that it can be found, not the content of any one
document.

---

Decisions affecting this skill: `docs/decisions/*-durable-context-*.md`
