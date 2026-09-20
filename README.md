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
| [fixtures](skills/fixtures/SKILL.md) | Test data comes from real-world capture, never invention. |

Planned: `linting`, `contracts`, `spec`, `definition-of-done`, `test-fidelity`, `harness`,
`project-setup`, `decision-log`, plus ports of `tdd` and `error-taxonomy`.

## Installation

### Claude Code

```
/plugin marketplace add ~/code/build-skills-cobarx
/plugin install build-skills-cobarx --scope user
```

To load temporarily without installing:

```bash
claude --plugin-dir ~/code/build-skills-cobarx
```

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
