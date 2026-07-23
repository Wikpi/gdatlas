import pytest

from pathlib import Path

from gdatlas.parser import parse_script
from gdatlas.model import Script

from gdatlas.parser.common import ParseContext

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
def test_parse_script(
    godot3_dir: Path,
    project_name: str,
    script_path: str,
    expected_functions: int,
    expected_variables: int,
) -> None:
    script = Script(path=godot3_dir / project_name / script_path)
    ctx = ParseContext(godot_version="3")

    parse_script(ctx, script)

    assert len(script.functions) == expected_functions
    assert len(script.variables) == expected_variables