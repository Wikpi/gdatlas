from gdatlas.model.script.metadata import ClassName
from gdatlas.parser.godot3.script import tokens


def parse_class_name(line: str, line_number: int) -> ClassName | None:
    if not line:
        return None

    prefix: str = f"{tokens.CLASS_NAME} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).strip()

    value = signature.strip()
    if not value:
        return None

    return ClassName(
        value=value,
        line_number=line_number,
    )
