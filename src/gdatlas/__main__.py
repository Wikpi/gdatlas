import sys
from pathlib import Path

from gdatlas.analyze import analyze_project
from gdatlas.parser import parse_project
from gdatlas.scanner import scan_project


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

    for script in project.scripts:
        print(f"Script: {script.path}")
        print(f" - Dependencies: {len(script.dependencies)}")

        for dependency in script.dependencies:
            print(f" - - Target: {dependency.target}")
            print(f" - - Source: {dependency.source}")


if __name__ == "__main__":
    main()
