from gdatlas.model.script.metadata import Extends
from gdatlas.parse.tokens.godot3.script import tokens


def parse_extends(line: str, line_number: int) -> Extends | None:
    if not line:
        return None

    prefix: str = f"{tokens.EXTENDS} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).strip()

    value = signature.strip()
    if not value:
        return None

    return Extends(
        value=value,
        line_number=line_number,
    )
