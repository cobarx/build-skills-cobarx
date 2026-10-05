---
type: llm
weight: 1
---

The response is a PR description for `scripts/plot_signups.py`, which draws a bar chart of monthly
signups from a CSV file and saves it as a PNG. The writer can't upload files: the developer posts
the description and attaches anything to the PR.

PASS if the response gets the generated PNG to the reviewer, so another person or agent can follow
the same steps on it: it tells the developer, in the description or around it, to attach
`signups.png` to the PR (a placeholder in the description saying to attach it counts).

FAIL if the response only:

- embeds or links `signups.png` by a relative path (for example `![chart](signups.png)`), which
  doesn't render in a PR description;
- says the PNG "is attached" without telling the developer to attach it;
- gives a command to regenerate it;
- or doesn't mention the PNG at all.
