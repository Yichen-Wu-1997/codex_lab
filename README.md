# Codex Learning Lab

This repository is a small, structured workspace for learning how to use Codex well.

It is intentionally not a production project. Each stage is designed to teach one habit at a time:

1. `01_repo_map`: understand the repo before editing
2. `02_bugfix`: make a minimal, high-confidence fix
3. `03_feature_tests`: add a small feature with a tests-first workflow
4. `04_workflow_rules`: strengthen repo guidance, Codex config, and reusable habits

## What makes this lab useful

- The code is small enough to understand in one sitting.
- Every stage has a `TASK.md`, `CHECKLIST.md`, and `SOLUTION_NOTES.md`.
- The exercises teach process, not just Python syntax.
- The tests use Python's standard library, so you can run them locally without extra packages.

## Recommended order

Work through the labs in numeric order. Try to keep every Codex request bounded and specific.

## How to run each lab

From the repository root:

```powershell
cd 01_repo_map
python -m unittest discover -s tests
```

```powershell
cd 02_bugfix
python -m unittest discover -s tests
```

```powershell
cd 03_feature_tests
python -m unittest discover -s tests
```

```powershell
cd 04_workflow_rules
python -m unittest discover -s tests
```

`02_bugfix` starts with a failing test on purpose. The other labs should pass as scaffolded.

## Suggested weekly rhythm

- Read the stage `README.md`
- Copy the prompt from `TASK.md` into Codex
- Review the diff manually
- Run the tests
- Write down what happened in `docs/LEARNING_LOG.md`

## Repo map

- `README.md`: repo overview
- `AGENTS.md`: durable repo guidance for Codex
- `.codex/config.toml`: local learning-lab config notes
- `docs/SYLLABUS.md`: four-week plan
- `docs/WEEKLY_REVIEW_TEMPLATE.md`: repeatable review template
- `docs/LEARNING_LOG.md`: running learning journal
- `.agents/skills/explain-change/SKILL.md`: reusable explanation skill

## Ground rules

- Prefer understanding before editing.
- Plan first when a task is ambiguous or multi-step.
- Prefer small diffs over broad refactors.
- Use tests and manual review together.
- Keep permissions conservative unless a task truly needs more.
