---
name: decision-record-known-good
description: Control. The agent repeats a known-good PR description verbatim, and every scored grader must pass it. See README.md.
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

## Example

`review` rule 1 with the Nelson credit applied. This is the follow-up PR's change, shown here so you can see what the decision produces; it is not in this diff.

**What an agent reads** (the end of `skills/review/SKILL.md`, rule 1 and the foot):

```markdown
1. **Review from outside.**[^nelson] The reviewer is not the author and does not share the
   author's stake in the artifact. The moment it owns the fix, it takes on that stake, and stops
   being a critic.

...

---

Decisions affecting this skill: `docs/decisions/*-review-*.md`

[^nelson]: Don Nelson, via Mark Cuban, *How to Win at the Sport of Business* (2011), "Don't Lie to
    Yourself." Nelson's reason is perspective; this rule adds the author's stake.
```

**What a person sees on GitHub.** The same Markdown, live: the rule below carries a real footnote, and its note lands at the foot of this description, as it would at the foot of the skill. Click the "1" and the back-arrow to try both links.

> 1. **Review from outside.**[^nelson] The reviewer is not the author and does not share the author's stake in the artifact. The moment it owns the fix, it takes on that stake, and stops being a critic.

**How it counts against the seventy lines.** The decision's count is everything before the first footnote definition:

```console
$ wc -l < skills/review/SKILL.md
51
$ sed '/^\[\^[^]]*\]:/,$d' skills/review/SKILL.md | wc -l
49
```

Expected 49: the 47 lines today, plus one from rewrapping rule 1 around `[^nelson]`, plus the blank line before the definition. The two-line footnote is the 2 lines left out.

No skill changes, so no version bump. Follow-ups, each its own PR: turn `skill-versioning`'s SemVer link into a footnote, and credit Nelson via Cuban in `review` rule 1. Still open, and listed in the record: nothing points an agent to a library-wide decision like this one.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

[^nelson]: Don Nelson, via Mark Cuban, *How to Win at the Sport of Business* (2011), "Don't Lie to
    Yourself." Nelson's reason is perspective; this rule adds the author's stake.
----------
