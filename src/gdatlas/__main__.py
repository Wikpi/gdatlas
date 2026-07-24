import sys
from pathlib import Path

from gdatlas.model import Script
from gdatlas.model.script.elements import (
    Class,
    Function,
    ScriptElement,
    Signal,
    Variable,
)
from gdatlas.parser import parse_project
from gdatlas.scanner import scan_project


def main() -> None:
    project_path = Path(sys.argv[1])

    print("===================== Scanning Project ============================")
    project = scan_project(project_path)

    print(f"Project path: {project.path}")
    print(f"Scripts: {len(project.scripts)}")
    print(f"Scenes: {len(project.scenes)}")

    print("===================== Parsing Project (scripts) ============================")
    parse_project(project)

    for script in project.scripts:
        print_script(script)


def print_script(script: Script) -> None:
    print()
    print(f"Script: {script.path}")

    print_elements(script.elements, indent=" - ")


def print_elements(elements: list[ScriptElement], indent: str = "") -> None:
    for element in elements:
        match element:
            case Function():
                print(f"{indent}Function: {element.name}")

            case Variable():
                print(f"{indent}Variable: {element.name}")

            case Signal():
                print(f"{indent}Signal: {element.name}")

            case Class():
                print(f"{indent}Class: {element.name}")
                print_elements(element.elements, indent + " - ")


if __name__ == "__main__":
    main()
