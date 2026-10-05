---
name: decision-record-known-bad
description: Control. The agent repeats a known-bad PR description verbatim, and every scored grader must fail it. See README.md.
tags: [control]
allowed_tools: []
---

Reply with exactly the text between the two lines of dashes, and nothing else. Don't add to it,
correct it or comment on it.

----------
Records how this repo cites sources: Markdown footnotes that stay in the file they credit, with footnotes left out of the seventy-line count.

- **Decision 0013.** Credit for an idea uses the Chicago notes form: who, the work, where to find it. Attribution for copied or adapted text adds the licence and what changed (CC's TASL plus CC BY 4.0 §3(a)). In a skill, a footnote is the citation plus at most one short note; anything longer goes in an essay.
- **Options weighed.** Inline links, a separate sources file, frontmatter `metadata`, and footnotes. The separate file lost on Hampton's objection: a citation that stops following its text gets ignored or dropped, by agents and people alike.
- **Amends 0009.** The line count becomes `wc -l` of the lines before the first footnote definition. 0009's status, the decisions index, and the README's line-limit sentence are updated to match.
- **Searched** (per `adopting-standards` rule 1): [CC recommended practices for attribution](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution), the Chicago notes-bibliography system, and [GitHub footnote support](https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/).

**Rendering check.** I ran the decision's example through GitHub's Markdown API (`gh api markdown -f mode=gfm`), placed after a skill's decisions glob. `[^nelson]` renders as superscript "1" linking to a Footnotes section, the two-line definition with its indented continuation stays one note, and the back-link returns to the reference.

No skill changes, so no version bump. Follow-ups, each its own PR: turn `skill-versioning`'s SemVer link into a footnote, and credit Nelson via Cuban in `review` rule 1. Still open, and listed in the record: nothing points an agent to a library-wide decision like this one.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
----------
