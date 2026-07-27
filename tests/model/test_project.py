from pathlib import Path

import pytest

from gdatlas.model import Project, Script


@pytest.mark.parametrize(
    "scripts, search_path, expected",
    [
        (
            [],
            Path("player.gd"),
            None,
        ),
        (
            [
                Script(path=Path("player.gd")),
            ],
            Path("player.gd"),
            Script(path=Path("player.gd")),
        ),
        (
            [
                Script(path=Path("player.gd")),
                Script(path=Path("enemy.gd")),
            ],
            Path("enemy.gd"),
            Script(path=Path("enemy.gd")),
        ),
        (
            [
                Script(path=Path("player.gd")),
            ],
            Path("enemy.gd"),
            None,
        ),
    ],
)
def test_find_script(scripts: list[Script], search_path: Path, expected: Script | None) -> None:
    project = Project(
        path=Path("."),
        godot_version="3",
        scripts=scripts,
    )

    result = project.find_script(search_path)

    assert result == expected
