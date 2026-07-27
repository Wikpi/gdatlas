from gdatlas.model.script.metadata import ScriptMetadata
from gdatlas.parser.godot3.script import tokens


def parse_class_name(line: str, line_number: int) -> ScriptMetadata | None:
    if not line:
        return None

    prefix: str = f"{tokens.CLASS_NAME} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).strip()

    value = signature.strip()
    if not value:
        return None

    return ScriptMetadata(
        name=tokens.CLASS_NAME,
        value=value,
        line_number=line_number,
    )
