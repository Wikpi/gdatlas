from gdatlas.model import Project

from .common import ParseContext
from .script_parser import parse_script


def parse_project(project: Project) -> Project:
    if not project:
        raise ValueError("Invalid Godot project.")

    ctx = ParseContext(godot_version=project.godot_version)

    for script in project.scripts:
        parse_script(ctx, script)

    return project
