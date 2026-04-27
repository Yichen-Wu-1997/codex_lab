# 02_bugfix

This stage is for minimal bug-fix practice.

The project is intentionally tiny. One test fails because of a boundary-condition bug. The right move is to diagnose the failure, make the smallest reasonable fix, rerun the tests, and review the diff.

## Goal

Practice asking Codex to:

- inspect the failing test first
- explain the bug before editing
- change as little code as possible
- verify the fix with tests

## Run the tests

```powershell
python -m unittest discover -s tests
```
