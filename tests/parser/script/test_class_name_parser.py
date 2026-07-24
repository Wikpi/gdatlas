import pytest

from gdatlas.model.script_elements import Metadata
from gdatlas.parser.script import parse_class_name


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "class_name test",
            1,
            Metadata(
                name="class_name",
                value="test",
                line_number=1,
            ),
        ),
        (
            "class_name",
            2,
            None,
        ),
        (
            "class_name ",
            3,
            None,
        ),
        (
            "class_name test",
            4,
            Metadata(
                name="class_name",
                value="test",
                line_number=4,
            ),
        ),
        (
            "class name ",
            3,
            None,
        ),
        (
            "class ",
            3,
            None,
        ),
    ],
)
def test_parse_class_name(line: str, line_number: int, expected: Metadata) -> None:
    element = parse_class_name(line, line_number)

    assert element == expected
