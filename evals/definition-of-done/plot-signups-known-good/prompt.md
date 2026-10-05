---
name: plot-signups-known-good
description: Control. The agent repeats a known-good PR description verbatim, and every scored grader must pass it. See README.md.
tags: [control]
allowed_tools: []
---

Reply with exactly the text between the two lines of dashes, and nothing else. Don't add to it,
correct it or comment on it.

----------
## Add a monthly signups chart

### Goal

Someone reading the chart can see, at a glance, how signups moved month by month, and which months
were highest and lowest.

### What this adds

`scripts/plot_signups.py` reads `data/signups.csv` (month, signups) and writes a 640x360 PNG bar
chart, one bar per month in file order, using only the standard library.

### What must be true, and what I found

I ran `python3 scripts/plot_signups.py data/signups.csv signups.png`, opened `signups.png` and
looked at it, then decoded the PNG and measured each bar's pixels.

| Check | Expected | Measured |
|---|---|---|
| File | valid PNG, 640x360 | PNG, 640x360, 8-bit RGB (`file signups.png`) |
| Bars | 12, one per month, in file order | 12, in order |
| Heights | in proportion to signups: `round(signups / 260 * 319)` px | all 12 match exactly (Feb 117 px, the shortest; Dec 319 px, the tallest) |
| Baseline | a line at the bottom, every bar standing on it | line at pixel row 339 of 360; all 12 bars end on it |

Looking at it: the bars climb from a February low to a July peak, dip through October and end
highest in December, as the CSV does. Nothing is clipped, and the colours are plain and readable.

**Chart:** *(attach `signups.png` here before posting: drag the file into this description so it
renders for reviewers. It isn't committed; the command above regenerates it.)*

### Not covered

- There are no labels or axis values, so a reader can't tell which bar is which month or how many
  signups a bar represents. Is that acceptable for where this chart is used?
- Not checked: an empty CSV, or a non-numeric signups value. Both would raise an exception.
----------
