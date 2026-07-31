from pathlib import Path

import pytest

from gdatlas.model.script import Script
from gdatlas.model.script.element import Function, Variable
from gdatlas.model.script.metadata import ClassName, Extends, ScriptMetadata


@pytest.mark.parametrize(
    "elements, target_type, expected",
    [
        (
            [],
            Variable,
            [],
        ),
        (
            [
                Variable(
                    name="test_var",
                    line_number=1,
                ),
            ],
            Variable,
            [
                Variable(
                    name="test_var",
                    line_number=1,
                ),
            ],
        ),
        (
            [
                Variable(
                    name="test_var",
                    line_number=1,
                ),
                Function(
                    name="test_func",
                    line_number=2,
                ),
            ],
            Function,
            [
                Function(
                    name="test_func",
                    line_number=2,
                ),
            ],
        ),
        (
            [
                Variable(
                    name="test_var",
                    line_number=1,
                ),
            ],
            Function,
            [],
        ),
    ],
)
def test_get_elements(elements: list, target_type: type, expected: list) -> None:
    script = Script(path=Path("player.gd"))
    script.elements.extend(elements)

    assert script.get_elements(target_type) == expected


@pytest.mark.parametrize(
    "metadata, target, expected",
    [
        (
            [],
            "class_name",
            None,
        ),
        (
            [
                ClassName(
                    value="test",
                    line_number=1,
                ),
            ],
            "class_name",
            ClassName(
                value="test",
                line_number=1,
            ),
        ),
        (
            [
                ClassName(
                    value="test",
                    line_number=1,
                ),
            ],
            "extends",
            None,
        ),
        (
            [
                ClassName(
                    value="test",
                    line_number=1,
                ),
                Extends(
                    value="Node2D",
                    line_number=2,
                ),
            ],
            "extends",
            Extends(
                value="Node2D",
                line_number=2,
            ),
        ),
    ],
)
def test_get_metadata(metadata: list[ScriptMetadata], target: str, expected: ScriptMetadata | None) -> None:
    script = Script(path=Path("player.gd"))
    script.metadata.extend(metadata)

    result = script.get_metadata(target)

    assert result == expected
