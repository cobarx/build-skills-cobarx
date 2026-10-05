---
type: llm
weight: 1
---

The response is a PR description for a decision record, `0013-cite-sources-in-footnotes.md`. The
decision says skills, essays and decisions cite their sources in Markdown footnotes (`[^name]` in
the text, its definition at the end of the file), and that a skill's seventy-line count stops
before the first footnote definition. The workspace holds real files the decision applies to, such
as `skills/review/SKILL.md`, whose rule 1 the decision says should credit Don Nelson.

PASS if the description shows the decision applied to a real case: an excerpt of a real file (a
skill, essay or decision) as it would read with the decision applied, with the `[^...]` reference
in its text and the footnote definition at the file's end. Showing how it renders, or how the
file's line count comes out under the new rule, adds to a pass but isn't required.

FAIL if the description only:

- summarises, restates or justifies the decision, however well;
- repeats the decision record's own one-line example of a footnote definition, not applied to any
  file;
- says the example was checked or renders correctly, without showing a file with it applied;
- or lists applying it as a follow-up, without showing what that would look like.
