import pytest

from gdatlas.model.script.expression import Load, Preload, ScriptExpression
from gdatlas.parse.script import parse_expression


@pytest.mark.parametrize(
    ("value", "line_number", "expected"),
    [
        pytest.param(
            "load('res://Test.gd')",
            1,
            Load(
                path="'res://Test.gd'",
                line_number=1,
            ),
            id="parse-load-expression",
        ),
        pytest.param(
            "preload('res://Test.gd')",
            2,
            Preload(
                path="'res://Test.gd'",
                line_number=2,
            ),
            id="parse-preload-expression",
        ),
        pytest.param(
            "load()",
            3,
            None,
            id="empty-load-expression",
        ),
        pytest.param(
            "preload()",
            4,
            None,
            id="empty-preload-expression",
        ),
        pytest.param(
            "load",
            5,
            None,
            id="missing-load-signature",
        ),
        pytest.param(
            "preload",
            6,
            None,
            id="missing-preload-signature",
        ),
        pytest.param(
            "",
            7,
            None,
            id="empty-expression",
        ),
    ],
)
def test_parse_expression(value: str, line_number: int, expected: ScriptExpression | None) -> None:
    expression = parse_expression(value, line_number)

    assert expression == expected
