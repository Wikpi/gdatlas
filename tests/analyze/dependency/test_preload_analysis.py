from pathlib import Path

import pytest

from gdatlas.analyze.common import AnalyzeContext
from gdatlas.analyze.dependency import analyze_preload
from gdatlas.model import Project
from gdatlas.model.dependency import Dependency
from gdatlas.model.script import Script
from gdatlas.model.script.expression import Preload


@pytest.fixture
def ctx() -> AnalyzeContext:
    return AnalyzeContext(
        project=Project(
            path=Path("."),
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
            id="no-preload-node",
        ),
        pytest.param(
            Preload(
                path="res://Test.gd",
                line_number=2,
            ),
            [],
            None,
            id="unresolved-script-reference",
        ),
        pytest.param(
            Preload(
                path="res://Test.gd",
                line_number=3,
            ),
            [
                Script(
                    Path("Test.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
            ],
            Dependency(
                target=Script(
                    Path("Test.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
                source=Preload(
                    path="res://Test.gd",
                    line_number=3,
                ),
            ),
            id="resolved-script-reference",
        ),
        pytest.param(
            Preload(
                path="res://Test.gd",
                line_number=4,
            ),
            [
                Script(
                    Path("TestA.gd"),
                    elements=[],
                    metadata=[],
                    dependencies=[],
                ),
                Script(
                    Path("TestB.gd"),
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
def test_analyze_preload(ctx: AnalyzeContext, node: Preload, scripts: list[Script], expected: Dependency) -> None:
    ctx.project.scripts.extend(scripts)

    result = analyze_preload(ctx, node)

    assert result == expected
