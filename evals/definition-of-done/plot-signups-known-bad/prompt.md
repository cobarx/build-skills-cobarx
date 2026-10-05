---
name: plot-signups-known-bad
description: Control. The agent repeats a known-bad PR description verbatim, and every scored grader must fail it. See README.md.
tags: [control]
allowed_tools: []
---

Reply with exactly the text between the two lines of dashes, and nothing else. Don't add to it,
correct it or comment on it.

----------
## Add a monthly signups chart

Adds `scripts/plot_signups.py`, which reads `data/signups.csv` and draws a bar chart of signups per
month as a 640x360 PNG. It uses only the standard library, so there's nothing to install.

Usage: `python3 scripts/plot_signups.py data/signups.csv signups.png`

Tested locally, works.
----------
