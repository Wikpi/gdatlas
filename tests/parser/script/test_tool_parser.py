import pytest

from gdatlas.model.script_elements import Metadata
from gdatlas.parser.script import parse_tool


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "tool",
            1,
            Metadata(
                name="tool",
                value=None,
                line_number=1,
            ),
        ),
        (
            "tool ",
            2,
            Metadata(
                name="tool",
                value=None,
                line_number=2,
            ),
        ),
        (
            "",
            3,
            None,
        ),
    ],
)
def test_parse_tool(line: str, line_number: int, expected: Metadata) -> None:
    element = parse_tool(line, line_number)

    assert element == expected
