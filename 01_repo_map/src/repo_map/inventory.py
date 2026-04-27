from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectFile:
    path: str
    area: str
    is_entry_point: bool = False


def sample_files() -> list[ProjectFile]:
    return [
        ProjectFile("src/repo_map/inventory.py", "source"),
        ProjectFile("src/repo_map/report.py", "source", is_entry_point=True),
        ProjectFile("tests/test_report.py", "tests"),
        ProjectFile("README.md", "docs", is_entry_point=True),
    ]
