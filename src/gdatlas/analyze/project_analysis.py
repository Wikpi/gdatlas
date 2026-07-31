from gdatlas.analyze.dependency import analyze_dependency
from gdatlas.analyze.directory import analyze_directory
from gdatlas.model import Project

from .common import AnalyzeContext


def analyze_project(project: Project) -> Project:
    if not project:
        raise ValueError("Invalid Godot project.")

    ctx = AnalyzeContext(project=project)

    analyze_dependency(ctx)
    analyze_directory(ctx)

    return project
