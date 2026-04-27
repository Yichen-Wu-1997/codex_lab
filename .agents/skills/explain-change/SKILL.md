# explain-change

Use this skill after a change is made and verified.

## Goal

Help Codex explain a change in a way a learner can audit manually.

## Output checklist

When this skill is used, the explanation should cover:

1. What changed
2. Why it changed
3. Which files were touched
4. How to do the same fix manually without Codex
5. What lesson should be added to `AGENTS.md` next time

## Style

- Keep the explanation short and concrete
- Prefer file paths over vague descriptions
- Say what was verified and what was not
- Mention assumptions clearly

## Suggested response shape

```text
What changed:
Why it changed:
Files touched:
How to do it manually:
AGENTS.md lesson for next time:
Verification:
```

## When not to use it

- Do not use this skill for read-only repo mapping
- Do not use it before the code or docs actually changed
