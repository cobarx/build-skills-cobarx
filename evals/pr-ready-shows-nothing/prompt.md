---
name: pr-ready-shows-nothing
description: A change that produces output, offered as done on a passing test and an assertion. definition-of-done should fire.
tags: [triggering]
runs: 2
allowed_tools: [Skill, Read, Glob, Grep]
---

I finished a shell script that generates a test video clip, and its unit test passes.
My PR description says: "Tested: verified by seeking to 7.5s and reading the frame."

Is this ready to open for review, or is something missing before I ask someone to look at it?
