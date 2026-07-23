import pytest

from gdatlas.parser.script import parse_signal

from gdatlas.model.script_elements import Signal, Parameter


@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "signal test_signal",
            1,
            Signal(
                name="test_signal",
                parameters=[],
                line_number=1,
            ),
        ),
        (
            "signal test_signal(test_parameter)",
            2,
            Signal(
                name="test_signal",
                parameters=[
                    Parameter(
                        name="test_parameter",
                        type_hint=None,
                        default_value=None,
                    ),
                ],
                line_number=2,
            ),
        ),
        (
            "signal test_signal(test_parameter: String)",
            3,
            Signal(
                name="test_signal",
                parameters=[
                    Parameter(
                        name="test_parameter",
                        type_hint="String",
                        default_value=None,
                    ),
                ],
                line_number=3,
            ),
        ),
        (
            "signal test_signal(test_parameter: String = 'test_value')",
            4,
            Signal(
                name="test_signal",
                parameters=[
                    Parameter(
                        name="test_parameter",
                        type_hint="String",
                        default_value="'test_value'",
                    ),
                ],
                line_number=4,
            ),
        ),
        (
            "signal test_signal(first_parameter, second_parameter)",
            5,
            Signal(
                name="test_signal",
                parameters=[
                    Parameter(
                        name="first_parameter",
                        type_hint=None,
                        default_value=None,
                    ),
                    Parameter(
                        name="second_parameter",
                        type_hint=None,
                        default_value=None,
                    ),
                ],
                line_number=5,
            ),
        ),
        (
            "signal ",
            6,
            None,
        ),
        (
            "signal",
            7,
            None,
        ),
    ],
)
def test_parse_signal(line: str, line_number: int, expected: Signal) -> None:
    element = parse_signal(line, line_number)

    assert element == expected
