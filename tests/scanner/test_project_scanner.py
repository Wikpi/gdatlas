import pytest

from pathlib import Path

from gdatlas.scanner.project_scanner import scan_project


@pytest.mark.parametrize(
    "project_name, expected_script_count, expected_scene_count",
    [
        ("minimal", 1, 1),
        ("empty", 0, 0),
    ],
)
def test_scan_projects(
    godot3_dir: Path,
    project_name: str,
    expected_script_count: int,
    expected_scene_count: int,
) -> None:
    project_path: Path = godot3_dir / project_name
    project = scan_project(project_path)

    assert project.path == project_path
    assert len(project.scripts) == expected_script_count
    assert len(project.scenes) == expected_scene_count


@pytest.mark.parametrize(
    "project_name, expected_error_type, expected_error_message",
    [
        ("missing_project_godot", ValueError, "Invalid Godot project path"),
        # ("invalid_structure", ValueError, "Invalid Godot structure"),
    ],
)
def test_invalid_projects(
    godot3_dir: Path,
    project_name: str,
    expected_error_type: str,
    expected_error_message: str,
) -> None:
    project_path: Path = godot3_dir / project_name

    with pytest.raises(expected_error_type, match=expected_error_message):
        scan_project(project_path)
