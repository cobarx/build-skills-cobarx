# build-skills-cobarx

Skills for how software gets built.

Each skill is a short set of rules, loaded by an AI coding assistant when it applies. They are
deliberately brief: a skill costs context every time it fires, so it holds rules and nothing else.
The reasoning behind them lives in [docs/essays/](docs/essays/).

## Skills

| Skill | Purpose |
|---|---|
| [simplicity](skills/simplicity/SKILL.md) | Bound the size of a unit of work. |
| [platform-correctness](skills/platform-correctness/SKILL.md) | Meet the conventions of the environment the software runs in. |
| [naming](skills/naming/SKILL.md) | A name tells the truth about the thing it names. |
| [format](skills/format/SKILL.md) | Remove formatting from human judgment. |
| [contracts](skills/contracts/SKILL.md) | Units meet only at explicit contracts, never internals. |
| [fixtures](skills/fixtures/SKILL.md) | Test data comes from the real world, or says that it does not. |
| [skill-versioning](skills/skill-versioning/SKILL.md) | Version the skill library by how its skills changed. |
| [parallel-work](skills/parallel-work/SKILL.md) | Isolate concurrent work at the cheapest level that prevents collisions. |
| [definition-of-done](skills/definition-of-done/SKILL.md) | Done is the goal met, and shown to be met. |
| [essays](skills/essays/SKILL.md) | An essay says who wrote it and how it has changed. |

Planned: `linting`, `spec`, `test-fidelity`, `harness`, `project-setup`,
`decision-log`, plus ports of `tdd` and `error-taxonomy`.

## Installation

### Claude Code

Install once, from this repo as a local marketplace:

```
/plugin marketplace add ~/code/build-skills-cobarx
/plugin install build-skills-cobarx@build-skills-cobarx --scope user
```

`--scope user` makes the skills available in every project.

To load temporarily without installing:

```bash
claude --plugin-dir ~/code/build-skills-cobarx
```

#### Updating

The marketplace points at this directory, so `git pull` is the update, with no copy step to go stale:

- Edited an existing skill: the next session picks it up, nothing else to do.
- Added or removed a skill: run `/plugin marketplace update build-skills-cobarx`.
- Check what is installed: run `/plugin`.

### GitHub Copilot CLI

```bash
ln -s ~/code/build-skills-cobarx/skills ~/.agents/skills/build-skills-cobarx
```

## How these are written

Two conventions do most of the work:

**The outline is the skill.** No expanded rationale, no worked examples where the rule is already
unambiguous. Every skill here is under sixty lines.

**Draft long, then keep only what is a rule.** The long draft is a discovery tool, not the
deliverable. The test applied to every line: does this change what anyone does? See
[docs/essays/outline-is-the-skill.md](docs/essays/outline-is-the-skill.md).

## Relationship to other repos

- [ai-skills-cobarx](https://github.com/cobarx/ai-skills-cobarx) covers a different domain and
  stays independently shareable.
- MetanoiaFramework is the source for several planned ports.
