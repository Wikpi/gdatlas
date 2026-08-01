from pathlib import Path

from gdatlas.model import Project, Scene
from gdatlas.model.script import Script

IGNORED_DIRECTORIES = {
    ".git",
    ".godot",
    ".import",
}


def scan_project(project_path: str) -> Project:
    project_path = Path(project_path)

    if not is_valid_project(project_path):
        raise ValueError(f"Invalid Godot project path: {project_path}")

    project_path = project_path.resolve()

    scripts: list[Script] = []
    scenes: list[Scene] = []

    for file in project_path.rglob("*"):
        if is_ignored_file(file):
            continue

        # relative_path: Path = file.relative_to(project_path)
        script_path: Path = file.resolve()

        if is_script(file):
            scripts.append(
                Script(
                    path=script_path,
                    metadata=[],
                    elements=[],
                    dependencies=[],
                ),
            )

        elif is_scene(file):
            scenes.append(
                Scene(
                    path=script_path,
                ),
            )

    # TODO: remove hardcoded version.
    return Project(
        path=project_path,
        godot_version="3",
        scripts=scripts,
        scenes=scenes,
    )


def is_ignored_file(path: Path) -> bool:
    return any(part in IGNORED_DIRECTORIES for part in path.parts)


def is_script(path: Path) -> bool:
    return path.suffix == ".gd"


def is_scene(path: Path) -> bool:
    return path.suffix == ".tscn"


def is_valid_project(path: Path) -> bool:
    return path.is_dir() and (path / "project.godot").exists()
