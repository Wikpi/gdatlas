import pytest

from gdatlas.model.script.elements import Class
from gdatlas.model.script.metadata import Extends
from gdatlas.parser.script import parse_inner_class


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "class TestClass:",
            1,
            Class(
                name="TestClass",
                metadata=[],
                elements=[],
                line_number=1,
            ),
        ),
        (
            "class TestExtend extends TestClass:",
            2,
            Class(
                name="TestExtend",
                metadata=[
                    Extends(
                        value="TestClass",
                        line_number=2,
                    ),
                ],
                elements=[],
                line_number=2,
            ),
        ),
        (
            "class",
            3,
            None,
        ),
        (
            "class ",
            4,
            None,
        ),
    ],
)
def test_parse_inner_class(line: str, line_number: int, expected: Class) -> None:
    node = parse_inner_class(line, line_number)

    assert node == expected
