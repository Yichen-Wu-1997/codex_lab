# AGENTS.md

This repository is a training workspace for learning Codex safely and systematically.

## Repo layout

- `01_repo_map/`: read-only understanding practice
- `02_bugfix/`: minimal bug-fix practice
- `03_feature_tests/`: small feature work with tests first
- `04_workflow_rules/`: repo guidance, configuration, and reusable workflow habits
- `docs/`: syllabus, review template, and learning log
- `.agents/skills/explain-change/`: tiny reusable explanation skill
- `.codex/config.toml`: local Codex learning-lab config

## How to run each lab

Run commands from the relevant lab directory.

### `01_repo_map`

```powershell
python -m unittest discover -s tests
```

### `02_bugfix`

```powershell
python -m unittest discover -s tests
```

This lab includes an intentional failing test before the fix.

### `03_feature_tests`

```powershell
python -m unittest discover -s tests
```

### `04_workflow_rules`

```powershell
python -m unittest discover -s tests
```

## Testing commands

- Preferred test command: `python -m unittest discover -s tests`
- If a task changes behavior, run the stage tests before and after the edit
- If a task only changes docs or guidance, explain why code tests were or were not needed

## Review expectations

- Read the relevant files before editing
- Summarize the plan before larger or multi-file changes
- Keep changes small and easy to review
- Inspect the diff after edits
- Say what was verified and what was not verified
- Note any assumptions instead of hiding them

## Constraints

- Prefer minimal changes over broad rewrites
- Explain before large edits
- Keep tasks bounded to one clear outcome
- Do not expand scope unless asked
- Keep permissions conservative unless a command truly needs more access
- Avoid introducing dependencies unless the learning value is clear

## Guidance for Codex

- In `01_repo_map`, default to read-only analysis unless the user explicitly asks for edits
- In `02_bugfix`, aim for the smallest fix that makes the failing test pass
- In `03_feature_tests`, write or update tests before implementation when adding behavior
- In `04_workflow_rules`, prefer durable instructions and reusable prompts over clever automation
- When a change spans several files, explain the intended edit set before modifying files
