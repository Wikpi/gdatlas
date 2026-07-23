from gdatlas.model.script_elements import Metadata


def parse_extends(line: str, line_number: int) -> Metadata | None:
    prefix: str = "extends "
    if not line.startswith(prefix):
        return None

    signature = line.removeprefix(prefix).strip()

    value = signature.strip()
    if not value:
        return None

    return Metadata(
        name="extends",
        value=value,
        line_number=line_number,
    )
