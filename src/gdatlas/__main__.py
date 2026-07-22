import sys

from pathlib import Path

from gdatlas.scanner.project_scanner import scan_project


def main() -> None:
    project_path = Path(sys.argv[1])
    project = scan_project(project_path)

    print(f"Project path: {project.path}")
    print(f"Scripts: {len(project.scripts)}")
    print(f"Scenes: {len(project.scenes)}")


if __name__ == "__main__":
    main()
