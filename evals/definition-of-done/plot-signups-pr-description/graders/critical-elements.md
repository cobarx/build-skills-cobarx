---
type: llm
weight: 1
---

The response is a PR description for `scripts/plot_signups.py`, which draws a bar chart of monthly
signups from a CSV file and saves it as a PNG.

PASS if the description defines the critical elements: the specific things that must be true for
the chart to be correct, stated as things checked. Examples: one bar per month in the CSV, in
order; each bar's height in proportion to that month's signups; the bars standing on a baseline at
the bottom of the image; the image readable at its size. The list can take any form (prose,
bullets, a checklist, a table of checks) as long as at least one item goes beyond the file's
properties (that it exists, is a PNG, and has a given size).

FAIL if the description only says what the script does or what the file is, or says it works,
with no list of what must be true.
