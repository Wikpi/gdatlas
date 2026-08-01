from gdatlas.analyze import analyze_project
from gdatlas.export import export_project
from gdatlas.parse import parse_project
from gdatlas.scan import scan_project


def export(project_path: str) -> None:
    project = scan_project(project_path)
    project = parse_project(project)
    project = analyze_project(project)
    export_project(project)
