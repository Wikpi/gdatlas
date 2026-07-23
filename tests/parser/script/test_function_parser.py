import pytest

from gdatlas.parser.script import parse_function

from gdatlas.model.script_elements import Function, Parameter

@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "func test_function(test_param: String = 'test_value') -> String",
            1,
            Function(
                name="test_function",
                parameters=[
                    Parameter(
                        name="test_param",
                        type_hint="String",
                        default_value="'test_value'",
                    ),
                ],
                return_type="String",
                line_number=1,
                static=False,
            ),
        ),
        (
            "func test_function()",
            2,
            Function(
                name="test_function",
                parameters=[],
                return_type=None,
                line_number=2,
                static=False,
            ),
        ),
        (
            "func test_function(first: int, second: float)",
            3,
            Function(
                name="test_function",
                parameters=[
                    Parameter(
                        name="first",
                        type_hint="int",
                        default_value=None,
                    ),
                    Parameter(
                        name="second",
                        type_hint="float",
                        default_value=None,
                    ),
                ],
                return_type=None,
                line_number=3,
                static=False,
            ),
        ),
        (
            "func test_function(first = 10, second = 20)",
            4,
            Function(
                name="test_function",
                parameters=[
                    Parameter(
                        name="first",
                        type_hint=None,
                        default_value="10",
                    ),
                    Parameter(
                        name="second",
                        type_hint=None,
                        default_value="20",
                    ),
                ],
                return_type=None,
                line_number=4,
                static=False,
            ),
        ),
        (
            "static func test_function() -> void",
            5,
            Function(
                name="test_function",
                parameters=[],
                return_type="void",
                line_number=5,
                static=True,
            ),
        ),
        (
            "func test_function(var value)",
            6,
            Function(
                name="test_function",
                parameters=[
                    Parameter(
                        name="value",
                        type_hint=None,
                        default_value=None,
                    ),
                ],
                return_type=None,
                line_number=6,
                static=False,
            ),
        ),
        (
            "func _ready()",
            7,
            Function(
                name="_ready",
                parameters=[],
                return_type=None,
                line_number=7,
                static=False,
            ),
        ),
        (
            "func",
            8,
            None,
        ),
        (
            "func ",
            9,
            None,
        ),
    ],
)
def test_parse_function(line: str, line_number: int, expected: Function) -> None:
    element = parse_function(line, line_number)

    assert element == expected