from pathlib import Path

import pytest

from gdatlas.model.script import Script
from gdatlas.model.script.element import Function, Variable
from gdatlas.parse.common import ParseContext
from gdatlas.parse.script import parse_script


@pytest.mark.parametrize(
    "project_name, script_path, expected_functions, expected_variables",
    [
        (
            "minimal",
            "test.gd",
            2,
            2,
        ),
    ],
)
def test_parse_script(godot3_dir: Path, project_name: str, script_path: str, expected_functions: int, expected_variables: int) -> None:
    script = Script(path=godot3_dir / project_name / script_path)
    ctx = ParseContext(godot_version="3")

    parse_script(ctx, script)

    function_count: int = 0
    variable_count: int = 0

    for node in script.elements:
        if isinstance(node, Function):
            function_count += 1
        elif isinstance(node, Variable):
            variable_count += 1

    assert function_count == expected_functions
    assert variable_count == expected_variables
