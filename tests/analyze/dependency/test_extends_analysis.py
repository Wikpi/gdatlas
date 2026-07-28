from pathlib import Path

import pytest

from gdatlas.analyze.common import AnalyzeContext
from gdatlas.analyze.script.dependency import analyze_extends
from gdatlas.model import Project
from gdatlas.model.dependency import Dependency
from gdatlas.model.script import Script
from gdatlas.model.script.metadata import ClassName, Extends


@pytest.fixture
def ctx() -> AnalyzeContext:
    return AnalyzeContext(
        project=Project(
            path=".",
            godot_version="3",
            scripts=[],
            scenes=[],
        ),
    )


@pytest.mark.parametrize(
    ("node", "scripts", "expected"),
    [
        pytest.param(
            None,
            [],
            None,
            id="no-extends-node",
        ),
        pytest.param(
            Extends(
                value="res://Test.gd",
                line_number=2,
            ),
            [
                Script(
                    Path("res://TestA.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
                Script(
                    Path("res://TestB.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
            ],
            None,
            id="missing-script-reference",
        ),
        pytest.param(
            Extends(
                value="res://Test.gd",
                line_number=3,
            ),
            [
                Script(
                    Path("res://Test.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
            ],
            Dependency(
                target=Script(
                    Path("res://Test.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
                source=Extends(
                    value="res://Test.gd",
                    line_number=3,
                ),
            ),
            id="resolve-script-reference-by-path",
        ),
        pytest.param(
            Extends(
                value="TestClass",
                line_number=4,
            ),
            [
                Script(
                    Path("res://Test.gd"),
                    elements=[],
                    metadata=[
                        ClassName(
                            value="TestClass",
                            line_number=1,
                        ),
                    ],
                    dependencies=[],
                ),
            ],
            Dependency(
                target=Script(
                    Path("res://Test.gd"),
                    elements=[],
                    metadata=[
                        ClassName(
                            value="TestClass",
                            line_number=1,
                        ),
                    ],
                    dependencies=[],
                ),
                source=Extends(
                    value="TestClass",
                    line_number=4,
                ),
            ),
            id="resolve-script-reference-by-class",
        ),
    ],
)
def test_analyze_extends(ctx: AnalyzeContext, node: Extends, scripts: list[Script], expected: Dependency) -> None:
    ctx.project.scripts.extend(scripts)

    result = analyze_extends(ctx, node)

    assert result == expected
