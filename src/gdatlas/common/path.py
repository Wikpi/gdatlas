from pathlib import Path


def resolve_local_path(path: str | Path, project_root: Path) -> Path:
    if isinstance(path, Path):
        path = str(path)
    if not path.startswith("res://"):
        return Path(path)
    return project_root / path.removeprefix("res://")


def is_path_reference(value: str) -> bool:
    return value.startswith("res://") or Path(value).is_absolute()
