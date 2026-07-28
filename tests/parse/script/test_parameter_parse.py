import pytest

from gdatlas.model.script.element import Parameter
from gdatlas.parse.script import parse_parameter


@pytest.mark.parametrize(
    "parameter, expected",
    [
        (
            "test_name: String = 'test_value'",
            Parameter(
                name="test_name",
                type_hint="String",
                default_value="'test_value'",
            ),
        ),
        (
            "test_name = 'test_value'",
            Parameter(
                name="test_name",
                type_hint=None,
                default_value="'test_value'",
            ),
        ),
        (
            "var test_name: String = 'test_value'",
            Parameter(
                name="test_name",
                type_hint="String",
                default_value="'test_value'",
            ),
        ),
        (
            "var test_name = 'test_value'",
            Parameter(
                name="test_name",
                type_hint=None,
                default_value="'test_value'",
            ),
        ),
        (
            "test_name: String",
            Parameter(
                name="test_name",
                type_hint="String",
                default_value=None,
            ),
        ),
        (
            "test_name",
            Parameter(
                name="test_name",
                type_hint=None,
                default_value=None,
            ),
        ),
        (
            "var test_name",
            Parameter(
                name="test_name",
                type_hint=None,
                default_value=None,
            ),
        ),
        (
            "",
            None,
        ),
        (
            "var ",
            None,
        ),
        (
            ":",
            None,
        ),
    ],
)
def test_parse_parameter(parameter: str, expected: Parameter) -> None:
    element = parse_parameter(parameter)

    assert element == expected
