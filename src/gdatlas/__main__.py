import sys
from pathlib import Path

from gdatlas.analyze import analyze_project
from gdatlas.export import export_project
from gdatlas.parse import parse_project
from gdatlas.scan import scan_project


def main() -> None:
    project_path = Path(sys.argv[1])

    print("===================== Scanning Project ============================")
    project = scan_project(project_path)

    print(f"Scenes: {len(project.scenes)}")
    print(f"Scripts: {len(project.scripts)}")

    print("===================== Parsing Project (scripts) ============================")
    project = parse_project(project)

    print("===================== Analyze Project (dependencies) ============================")
    project = analyze_project(project)

    print("===================== Reporting Project (dependency graph) ============================")
    project = export_project(project)


if __name__ == "__main__":
    main()
