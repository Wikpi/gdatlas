from .common import ParseContext
from .script_parser import parse_script

from gdatlas.model import Project


def parse_project(project: Project) -> None:
    ctx = ParseContext(godot_version=project.godot_version)

    for script in project.scripts:
        parse_script(ctx, script)
