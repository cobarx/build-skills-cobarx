# build-skills-cobarx

Skills for how software gets built.

Each skill is a short set of rules, loaded by an AI coding assistant when it applies. They are
deliberately brief: a skill costs context every time it fires, so it holds rules and nothing else.
The reasoning behind them lives in [docs/essays/](docs/essays/).

## Lineage

The skills are a close match for total quality management (TQM). TQM holds that quality is defined
by the customer and built into the work by everyone who does it, not checked for at the end.
[Quality is defined by the customer](docs/essays/quality-is-defined-by-the-customer.md) explains TQM
for a reader new to it and shows where the skills match it. TQM grew from the work of W. Edwards
Deming.

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
| [decision-analysis](skills/decision-analysis/SKILL.md) | Give the decider what they need to weigh a choice themselves. |
| [adopting-standards](skills/adopting-standards/SKILL.md) | Adopt an existing standard before inventing your own. |

Planned: `linting`, `test-fidelity`, `glossary`, `harness`, `project-setup`, a skill for the *why*
behind a goal (name not settled), plus ports of `tdd` and `error-taxonomy`.

## Installation

### Claude Code

Install from GitHub, for every project on this machine:

```bash
claude plugin marketplace add cobarx/build-skills-cobarx
claude plugin install build-skills-cobarx@build-skills-cobarx
```

Inside a session, `/plugin marketplace add cobarx/build-skills-cobarx` then
`/plugin install build-skills-cobarx@build-skills-cobarx` does the same, and asks for a scope.

The plugin's session-start hook puts `simplicity` in context at the start of every session,
because it applies to every unit of work. The other skills load when they apply.

#### Updating

Auto-update is off by default for marketplaces outside Anthropic's own. Either turn it on
(`/plugin`, **Marketplaces** tab, select `build-skills-cobarx`, **Enable auto-update**), or update
by hand:

```bash
claude plugin update build-skills-cobarx@build-skills-cobarx
```

`plugin.json` sets a version, so an update arrives when that version changes.

#### From a clone

To work on the skills, point the marketplace at your clone instead, so `git pull` is the update:

```bash
claude plugin marketplace add ./build-skills-cobarx
claude plugin install build-skills-cobarx@build-skills-cobarx
```

Run that from the directory that holds the clone. Edits to an existing skill load in the next
session; after adding or removing a skill, run `/plugin marketplace update build-skills-cobarx`.
To load a clone for one session without installing, use `claude --plugin-dir ./build-skills-cobarx`.

### Other agents

OpenAI Codex, GitHub Copilot (CLI, VS Code, JetBrains), Cursor, and Gemini CLI read the same
[Agent Skills](https://agentskills.io) format, and all four load skills from `~/.agents/skills/`.
Install there with the GitHub CLI:

```bash
gh skill install cobarx/build-skills-cobarx --all --dir ~/.agents/skills
```

Update with `gh skill update --all`. For an agent with its own directory, swap `--dir` for
`--agent <name> --scope user`; `gh skill install --help` lists the names. `gh skill` is in preview
in the GitHub CLI.

Without the GitHub CLI, copy each folder under `skills/` into `~/.agents/skills/`, one folder per
skill, directly under that directory.

These agents don't run the Claude Code hook yet, so `simplicity` loads only when its description
matches. Support for each is tracked in #134.

## How these are written

Two conventions do most of the work:

**The outline is the skill.** No expanded rationale, no worked examples where the rule is already
unambiguous. No skill here runs past seventy lines, not counting footnoted citations.

**Draft long, then keep only what is a rule.** The long draft is a discovery tool, not the
deliverable. The test applied to every line: does this change what anyone does? See
[docs/essays/outline-is-the-skill.md](docs/essays/outline-is-the-skill.md).

## License

The skills and documentation are licensed under [CC BY 4.0](LICENSE), © 2026 Hampton Maxwell.
Everything under `evals/`, prose, data, and code alike, is licensed under
[Apache-2.0](evals/LICENSE) instead. See [0014](docs/decisions/0014-license-cc-by-4-0.md) and
[0019](docs/decisions/0019-evals-take-apache-2-0.md).

To credit a skill you copy or adapt, give its title, author, source, licence, and what you
changed:

> Adapted from "simplicity" by Hampton Maxwell,
> <https://github.com/cobarx/build-skills-cobarx>, CC BY 4.0. Changes: …
