# build-skills-cobarx

Skills for how software gets built.

Each skill is a short set of rules, loaded by an AI coding assistant when it applies. They are
deliberately brief: a skill costs context every time it fires, so it holds rules and nothing else.
The reasoning behind them lives in [docs/essays/](docs/essays/).

## Skills

| Skill | Purpose |
|---|---|
| [simplicity](skills/simplicity/SKILL.md) | Make every change cheap to understand. |
| [platform-correctness](skills/platform-correctness/SKILL.md) | Meet the conventions of the environment the software runs in. |
| [naming](skills/naming/SKILL.md) | A name tells the truth about the thing it names. |
| [format](skills/format/SKILL.md) | Remove formatting from human judgment. |
| [contracts](skills/contracts/SKILL.md) | Units meet only at explicit contracts, never internals. |
| [fixtures](skills/fixtures/SKILL.md) | Test data comes from the real world, or says that it does not. |
| [skill-versioning](skills/skill-versioning/SKILL.md) | Version the skill library by how its skills changed. |
| [parallel-work](skills/parallel-work/SKILL.md) | Isolate concurrent units of work at the lowest level that prevents them from colliding. |
| [definition-of-done](skills/definition-of-done/SKILL.md) | Done is the goal shown to be met. |
| [essays](skills/essays/SKILL.md) | An essay carries its provenance. |
| [review](skills/review/SKILL.md) | A reviewer tries to break the work against the standard it claims to meet. |
| [durable-context](skills/durable-context/SKILL.md) | Context lives in the project, where the next reader, human or agent, will find it. |
| [spec](skills/spec/SKILL.md) | Say what the system must do before choosing how. |
| [decision-log](skills/decision-log/SKILL.md) | A decision is reasoned in the open. |
| [adopting-standards](skills/adopting-standards/SKILL.md) | Adopt an existing standard before inventing your own. |

Planned: `linting`, `test-fidelity`, `glossary`, `harness`, `project-setup`, a skill for the *why*
behind a goal (name not settled), plus ports of `tdd` and `error-taxonomy`.

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
unambiguous. No skill here runs past seventy lines.

**Draft long, then keep only what is a rule.** The long draft is a discovery tool, not the
deliverable. The test applied to every line: does this change what anyone does? See
[docs/essays/outline-is-the-skill.md](docs/essays/outline-is-the-skill.md).

## Relationship to other repos

- [ai-skills-cobarx](https://github.com/cobarx/ai-skills-cobarx) covers a different domain and
  stays independently shareable.
- MetanoiaFramework is the source for several planned ports.

## License

The skills and documentation are licensed under [CC BY 4.0](LICENSE), © 2026 Hampton Maxwell.
Code, when the repo has any, takes a software licence stated where it lives. See
[0014](docs/decisions/0014-license-cc-by-4-0.md).

To credit a skill you copy or adapt, give its title, author, source, licence, and what you
changed:

> Adapted from "simplicity" by Hampton Maxwell,
> <https://github.com/cobarx/build-skills-cobarx>, CC BY 4.0. Changes: …
