from gdatlas.export.dependency import export_dependency_graph
from gdatlas.model import Project


def export_project(project) -> Project:
    if not project:
        raise ValueError("Invalid Godot project.")

    export_dependency_graph(
        project=project,
        output_file="dependencies.svg",  # TODO: add custom file name + format input.
        output_path=project.path,  # TODO: add config ouput path selection.
    )

    return project
