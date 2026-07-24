import pytest

from gdatlas.model.script.elements import Variable
from gdatlas.parser.script import parse_variable


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "var test_variable",
            1,
            Variable(
                name="test_variable",
                type_hint=None,
                default_value=None,
                static=False,
                export=False,
                onready=False,
                line_number=1,
            ),
        ),
        (
            "var test_variable: String",
            2,
            Variable(
                name="test_variable",
                type_hint="String",
                default_value=None,
                static=False,
                export=False,
                onready=False,
                line_number=2,
            ),
        ),
        (
            "var test_variable = 'test_value'",
            3,
            Variable(
                name="test_variable",
                type_hint=None,
                default_value="'test_value'",
                static=False,
                export=False,
                onready=False,
                line_number=3,
            ),
        ),
        (
            "var test_variable: String = 'test_value'",
            4,
            Variable(
                name="test_variable",
                type_hint="String",
                default_value="'test_value'",
                static=False,
                export=False,
                onready=False,
                line_number=4,
            ),
        ),
        (
            "onready var test_variable = $TestNode",
            5,
            Variable(
                name="test_variable",
                type_hint=None,
                default_value="$TestNode",
                static=False,
                export=False,
                onready=True,
                line_number=5,
            ),
        ),
        (
            "export var test_variable: String",
            6,
            Variable(
                name="test_variable",
                type_hint="String",
                default_value=None,
                static=False,
                export=True,
                onready=False,
                line_number=6,
            ),
        ),
        (
            "static var test_variable = 10",
            7,
            Variable(
                name="test_variable",
                type_hint=None,
                default_value="10",
                static=True,
                export=False,
                onready=False,
                line_number=7,
            ),
        ),
        (
            "export onready var test_variable",
            8,
            Variable(
                name="test_variable",
                type_hint=None,
                default_value=None,
                static=False,
                export=True,
                onready=True,
                line_number=8,
            ),
        ),
        (
            "var",
            9,
            None,
        ),
        (
            "var ",
            10,
            None,
        ),
        (
            ":",
            11,
            None,
        ),
    ],
)
def test_parse_variable(line: str, line_number: int, expected: Variable) -> None:
    element = parse_variable(line, line_number)

    assert element == expected
