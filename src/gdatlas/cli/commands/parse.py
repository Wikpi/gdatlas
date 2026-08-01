from gdatlas.parse import parse_project
from gdatlas.scan import scan_project


def parse(project_path: str) -> None:
    project = scan_project(project_path)
    project = parse_project(project)
