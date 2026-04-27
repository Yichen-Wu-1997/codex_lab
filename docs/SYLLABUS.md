# Four-Week Codex Syllabus

## Week 1: Repo Understanding

Goal: learn to ask Codex for analysis before edits.

- Work in `01_repo_map`
- Ask Codex to map the repo, entry points, and module responsibilities
- Practice asking for a plan without requesting code changes
- Review whether Codex read the right files first

## Week 2: Bugfix + Diff Review

Goal: learn to make the smallest fix that solves a real failing test.

- Work in `02_bugfix`
- Ask Codex to diagnose the failure before editing
- Expect one focused code change and a quick verification step
- Review the diff closely and check whether scope stayed small

## Week 3: Feature + Tests

Goal: learn a tests-first workflow for a new behavior.

- Work in `03_feature_tests`
- Ask Codex to write or update tests before implementation
- Add one small feature only
- Review whether the tests describe the new behavior clearly

## Week 4: AGENTS.md + Config + Skill

Goal: learn to improve repo guidance so future sessions go better.

- Work in `04_workflow_rules`
- Update `AGENTS.md` with a useful lesson from earlier weeks
- Review `.codex/config.toml` and keep it conservative
- Use the reusable `explain-change` skill to make the outcome easier to understand

## Success criteria

By the end of four weeks, you should be comfortable asking Codex to:

- inspect a repo before editing
- propose a plan for multi-step work
- keep fixes minimal
- verify changes with tests
- explain a diff clearly
- improve repo-specific instructions for future sessions
