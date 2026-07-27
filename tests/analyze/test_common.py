from pathlib import Path

import pytest

from gdatlas.analyze.common import AnalyzeContext
from gdatlas.model import Project
from gdatlas.model.script import Script
from gdatlas.model.script.metadata import ClassName


@pytest.mark.parametrize(
    ("reference", "scripts", "expected"),
    [
        pytest.param(
            "",
            [],
            None,
            id="no-reference",
        ),
        pytest.param(
            Path("res://Test.gd"),
            [
                Script(
                    path=Path("res://Test.gd"),
                    metadata=[],
                    elements=[],
                    dependencies=[],
                ),
            ],
            Script(
                path=Path("res://Test.gd"),
                metadata=[],
                elements=[],
                dependencies=[],
            ),
            id="resolve-script-by-path",
        ),
        pytest.param(
            "TestClass",
            [
                Script(
                    path=Path("res://Test.gd"),
                    metadata=[
                        ClassName(
                            value="TestClass",
                            line_number=1,
                        )
                    ],
                    elements=[],
                    dependencies=[],
                ),
            ],
            Script(
                path=Path("res://Test.gd"),
                metadata=[
                    ClassName(
                        value="TestClass",
                        line_number=1,
                    )
                ],
                elements=[],
                dependencies=[],
            ),
            id="resolve-script-by-class",
        ),
        pytest.param(
            Path("res://Test.gd"),
            [
                Script(
                    path=Path("res://TestA.gd"),
                    metadata=[],
                    elements=[],
                    dependencies=[],
                ),
                Script(
                    path=Path("res://TestB.gd"),
                    metadata=[],
                    elements=[],
                    dependencies=[],
                ),
            ],
            None,
            id="missing-script",
        ),
    ],
)
def test_resolve_script_reference(reference: str | Path, scripts: list[Script], expected: Script) -> None:
    ctx = AnalyzeContext(
        project=Project(
            path=".",
            godot_version="3",
            scripts=scripts,
            scenes=[],
        ),
    )

    result = ctx.resolve_script_reference(reference)

    assert result == expected
