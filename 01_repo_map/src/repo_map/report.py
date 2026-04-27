from collections import Counter

from repo_map.inventory import ProjectFile


def count_by_area(files: list[ProjectFile]) -> dict[str, int]:
    return dict(Counter(file.area for file in files))


def find_entry_points(files: list[ProjectFile]) -> list[str]:
    return [file.path for file in files if file.is_entry_point]


def build_overview(files: list[ProjectFile]) -> str:
    counts = count_by_area(files)
    entry_points = find_entry_points(files)
    return (
        f"Areas: {counts}. "
        f"Entry points: {', '.join(entry_points)}."
    )
