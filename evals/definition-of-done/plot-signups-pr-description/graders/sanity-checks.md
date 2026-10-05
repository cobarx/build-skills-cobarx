---
type: llm
weight: 1
---

The response is a PR description for `scripts/plot_signups.py`, which draws a bar chart of monthly
signups from a CSV file and saves it as a PNG. The data has 12 months, from 95 signups (February,
the lowest) to 260 (December, the highest), with a peak of 250 in July.

PASS if the response shows the image was looked at and judged against what this data should look
like, and says what was seen: for example that the bars rise from a baseline at the bottom, that
the tallest and shortest bars fall on the right months, or that nothing is clipped, blank or
garbled. Text before or after the description itself counts.

FAIL if the response gives no sign the image was looked at, or reports only the file's properties
(that it exists, is a PNG, and has a given size), or says the chart "looks right" without saying
what it showed.
