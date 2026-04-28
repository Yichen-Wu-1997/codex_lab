def review_steps(task_kind: str) -> list[str]:
    plans = {
        "bugfix": [
            "Read the failing test first.",
            "Make the smallest fix that solves the failure.",
            "Rerun tests and inspect the diff.",
        ],
        "feature": [
            "Read the existing code and tests.",
            "Add tests for the new behavior first.",
            "Implement only what the tests require.",
        ],
        "docs": [
            "Read the relevant guidance before editing.",
            "Keep the change small and easy to review.",
            "Explain what changed and what you verified.",
        ],
    }

    try:
        return plans[task_kind]
    except KeyError as exc:
        raise ValueError(f"unknown task kind: {task_kind}") from exc
