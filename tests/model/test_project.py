from pathlib import Path

import pytest

from gdatlas.model import Project, Script


@pytest.mark.parametrize(
    "scripts, search_path, expected",
    [
        (
            [],
            Path("test.gd"),
            None,
        ),
        (
            [
                Script(path=Path("test.gd")),
            ],
            Path("test.gd"),
            Script(path=Path("test.gd")),
        ),
        (
            [
                Script(path=Path("testA.gd")),
                Script(path=Path("testB.gd")),
            ],
            Path("testB.gd"),
            Script(path=Path("testB.gd")),
        ),
        (
            [
                Script(path=Path("testA.gd")),
            ],
            Path("testB.gd"),
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
