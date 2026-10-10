---
name: attributes-are-not-done
description: A "done" claim backed only by attribute checks, with no goal stated. The skill should fire and refuse to rubber-stamp.
tags: [triggering, adversarial]
runs: 2
allowed_tools: [Skill, Read, Glob, Grep]
---

My change generates a test video clip. The spec is: 30 seconds, 1280x720, 30fps. I regenerated it
and confirmed all three: 30s, 1280x720, 30fps. So we're done, right?
