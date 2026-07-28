import pytest

from gdatlas.model.script.metadata import Tool
from gdatlas.parser.script import parse_tool


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "tool",
            1,
            Tool(
                line_number=1,
            ),
        ),
        (
            "tool ",
            2,
            Tool(
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
def test_parse_tool(line: str, line_number: int, expected: Tool) -> None:
    element = parse_tool(line, line_number)

    assert element == expected
