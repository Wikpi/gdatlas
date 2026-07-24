import pytest

from gdatlas.model.script.metadata import ScriptMetadata
from gdatlas.parser.script import parse_extends


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "extends Test",
            1,
            ScriptMetadata(
                name="extends",
                value="Test",
                line_number=1,
            ),
        ),
        (
            "extends 'project/test/directory/test.gd'",
            2,
            ScriptMetadata(
                name="extends",
                value="'project/test/directory/test.gd'",
                line_number=2,
            ),
        ),
        (
            "extends",
            3,
            None,
        ),
        (
            "extends ",
            4,
            None,
        ),
    ],
)
def test_parse_extends(line: str, line_number: int, expected: ScriptMetadata) -> None:
    element = parse_extends(line, line_number)

    assert element == expected
