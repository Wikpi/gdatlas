from pathlib import Path

import pytest

from gdatlas.analyze.common import AnalyzeContext
from gdatlas.analyze.dependency import analyze_load
from gdatlas.model import Project
from gdatlas.model.dependency import Dependency
from gdatlas.model.script import Script
from gdatlas.model.script.expressions import Load


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
            id="no-load-node",
        ),
        pytest.param(
            Load(
                path="res://Test.gd",
                line_number=2,
            ),
            [],
            None,
            id="unresolved-script-reference",
        ),
        pytest.param(
            Load(
                path="res://Test.gd",
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
                source=Load(
                    path="res://Test.gd",
                    line_number=3,
                ),
            ),
            id="resolved-script-reference",
        ),
        pytest.param(
            Load(
                path="res://Test.gd",
                line_number=4,
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
    ],
)
def test_analyze_load(ctx: AnalyzeContext, node: Load, scripts: list[Script], expected: Dependency) -> None:
    ctx.project.scripts.extend(scripts)

    result = analyze_load(ctx, node)

    assert result == expected
