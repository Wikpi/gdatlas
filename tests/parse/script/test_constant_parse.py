import pytest

from gdatlas.model.script.element import Constant
from gdatlas.parse.script import parse_constant


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "const TEST_NAME: String = 'test_value'",
            1,
            Constant(
                name="TEST_NAME",
                value="'test_value'",
                type_hint="String",
                line_number=1,
            ),
        ),
        (
            "const TEST_NAME = 'test_value'",
            2,
            Constant(
                name="TEST_NAME",
                value="'test_value'",
                type_hint=None,
                line_number=2,
            ),
        ),
        (
            "const test_name",
            3,
            None,
        ),
        (
            "const ",
            4,
            None,
        ),
        (
            "const",
            5,
            None,
        ),
    ],
)
def test_parse_constant(line: str, line_number: int, expected: Constant) -> None:
    element = parse_constant(line, line_number)

    assert element == expected
