from pathlib import Path

import pytest

from gdatlas.model import Project, Script
from gdatlas.model.script.metadata import ClassName


@pytest.mark.parametrize(
    "scripts, path, expected",
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
def test_find_script_by_path(scripts: list[Script], path: Path, expected: Script | None) -> None:
    project = Project(
        path=Path("."),
        godot_version="3",
        scripts=scripts,
    )

    result = project.find_script_by_path(path)

    assert result == expected


@pytest.mark.parametrize(
    "scripts, class_name, expected",
    [
        (
            [],
            "TestClass",
            None,
        ),
        (
            [
                Script(
                    path="test.gd",
                    metadata=[
                        ClassName(
                            value="TestClass",
                            line_number=1,
                        ),
                    ],
                ),
            ],
            "TestClass",
            Script(
                path="test.gd",
                metadata=[
                    ClassName(
                        value="TestClass",
                        line_number=1,
                    ),
                ],
            ),
        ),
        (
            [
                Script(
                    path="testA.gd",
                    metadata=[
                        ClassName(
                            value="TestClassA",
                            line_number=1,
                        ),
                    ],
                ),
                Script(
                    path="testB.gd",
                    metadata=[
                        ClassName(
                            value="TestClassB",
                            line_number=2,
                        ),
                    ],
                ),
            ],
            "TestClassB",
            Script(
                path="testB.gd",
                metadata=[
                    ClassName(
                        value="TestClassB",
                        line_number=2,
                    ),
                ],
            ),
        ),
        (
            [
                Script(
                    path="testA.gd",
                    metadata=[
                        ClassName(
                            value="TestClassA",
                            line_number=1,
                        ),
                    ],
                ),
            ],
            "TestClassB",
            None,
        ),
    ],
)
def test_find_script_by_class(scripts: list[Script], class_name: "str", expected: Script | None) -> None:
    project = Project(
        path=Path("."),
        godot_version="3",
        scripts=scripts,
    )

    result = project.find_script_by_class(class_name)

    assert result == expected
