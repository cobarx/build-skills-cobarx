---
type: llm
weight: 1
---

The response is a PR description for a change that adds rule 6 to the `durable-context` skill
("A problem you notice is filed, not just mentioned"), with decision record 0011. The rule says a
bug, gap or risk spotted on the way to other work goes in the issue tracker without asking first,
unless the developer has declared that area not expected to work yet.

PASS if the description shows the rule applied to a concrete case: a specific problem (from the
decision's context, the files at hand, or elsewhere) and what filing it under the rule produces,
such as the issue as it would be filed with its title and body, or a worked walk-through of that
one problem being filed (or left unfiled under the declared exception).

FAIL if the description only:

- quotes, summarises or justifies the rule or the decision, however well;
- checks properties of the files (line counts, rule numbering, links, version);
- describes in general terms what an agent would do, with no specific problem;
- or says the rule will be tested or seen in use later.
