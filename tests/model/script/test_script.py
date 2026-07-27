from pathlib import Path

import pytest

from gdatlas.model.script import Script
from gdatlas.model.script.elements import Function, Variable
from gdatlas.model.script.metadata import ScriptMetadata


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
                    name="health",
                    line_number=1,
                ),
            ],
            Variable,
            [
                Variable(
                    name="health",
                    line_number=1,
                ),
            ],
        ),
        (
            [
                Variable(
                    name="health",
                    line_number=1,
                ),
                Function(
                    name="ready",
                    line_number=2,
                ),
            ],
            Function,
            [
                Function(
                    name="ready",
                    line_number=2,
                ),
            ],
        ),
        (
            [
                Variable(
                    name="health",
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
                ScriptMetadata(
                    name="class_name",
                    value="Player",
                    line_number=1,
                ),
            ],
            "class_name",
            ScriptMetadata(
                name="class_name",
                value="Player",
                line_number=1,
            ),
        ),
        (
            [
                ScriptMetadata(
                    name="class_name",
                    value="Player",
                    line_number=1,
                ),
            ],
            "extends",
            None,
        ),
        (
            [
                ScriptMetadata(
                    name="class_name",
                    value="Player",
                    line_number=1,
                ),
                ScriptMetadata(
                    name="extends",
                    value="Node2D",
                    line_number=2,
                ),
            ],
            "extends",
            ScriptMetadata(
                name="extends",
                value="Node2D",
                line_number=2,
            ),
        ),
    ],
)
def test_get_metadata(
    metadata: list[ScriptMetadata],
    target: str,
    expected: ScriptMetadata | None,
) -> None:
    script = Script(path=Path("player.gd"))
    script.metadata.extend(metadata)

    result = script.get_metadata(target)

    assert result == expected
