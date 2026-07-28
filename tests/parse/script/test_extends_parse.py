import pytest

from gdatlas.model.script.metadata import Extends
from gdatlas.parse.script import parse_extends


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "extends Test",
            1,
            Extends(
                value="Test",
                line_number=1,
            ),
        ),
        (
            "extends 'project/test/directory/test.gd'",
            2,
            Extends(
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
def test_parse_extends(line: str, line_number: int, expected: Extends) -> None:
    element = parse_extends(line, line_number)

    assert element == expected
