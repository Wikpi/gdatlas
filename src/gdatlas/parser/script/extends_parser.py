from gdatlas.model.script.metadata import ScriptMetadata


def parse_extends(line: str, line_number: int) -> ScriptMetadata | None:
    prefix: str = "extends "
    if not line.startswith(prefix):
        return None

    signature = line.removeprefix(prefix).strip()

    value = signature.strip()
    if not value:
        return None

    return ScriptMetadata(
        name="extends",
        value=value,
        line_number=line_number,
    )
