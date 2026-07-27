from gdatlas.model import Project

from .common import AnalyzeContext
from .script_analysis import analyze_script


def analyze_project(project: Project) -> Project:
    if not project:
        raise ValueError("Invalid Godot project.")

    ctx = AnalyzeContext(project=project)

    for script in project.scripts:
        analyze_script(ctx, script)

    return project
