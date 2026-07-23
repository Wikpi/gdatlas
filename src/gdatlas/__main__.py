import sys

from pathlib import Path

from gdatlas.scanner import scan_project
from gdatlas.parser import parse_project

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

    print(f" - Metadata: {len(script.metadata)}")
    for metadata in script.metadata:
        if metadata.value != None:
            print(f" - - Property: \t{metadata.name}: {metadata.value};")
        else:
            print(f" - - Property: \t{metadata.name}")

    print(f" - Functions: {len(script.functions)}")
    for function in script.functions:
        print(f" - - Name: \t{function.name}")

        print(f" - - - Parameters: {len(function.parameters)}")
        for parameter in function.parameters:
            print(f" - - - - Name: \t{parameter.name}")
            if parameter.type_hint:
                print(f" - - - - - Type Hint: \t{parameter.type_hint};")
            if parameter.default_value:
                print(f" - - - - - Default Value: \t{parameter.default_value};")

        if function.return_type:
            print(f" - - - Return Type: \t{function.return_type};")

    print(f" - Variables: {len(script.variables)}")
    for variable in script.variables:
        print(f" - - Name: \t{variable.name}")
        if variable.type_hint:
            print(f" - - - Type Hint: \t{variable.type_hint};")
        if variable.default_value:
            print(f" - - - Default Value: \t{variable.default_value};")
        if variable.static:
            print(f" - - - Static: \ttrue;")
        if variable.onready:
            print(f" - - - Onready: \ttrue;")
        if variable.export:
            print(f" - - - Export: \ttrue;")

    print(f" - Signals: {len(script.signals)}")
    for signal in script.signals:
        print(f" - - Name: \t{signal.name}")
        print(f" - - - Parameters: {len(signal.parameters)}")
        for parameter in signal.parameters:
            print(f" - - - - Name: \t{parameter.name};")
            print(f" - - - - - Type Hint: \t{parameter.type_hint};")
            print(f" - - - - - Default Value: \t{parameter.default_value};")

if __name__ == "__main__":
    main()
