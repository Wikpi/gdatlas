from gdatlas.model.script.element import Constant
from gdatlas.parse.tokens.godot3.script import tokens

from .expression_parse import parse_expression


def parse_constant(line: str, line_number: int) -> Constant | None:
    if not line:
        return None

    prefix: str = f"{tokens.CONSTANT} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).strip()

    parts = signature.split("=", maxsplit=1)

    if len(parts) < 2:
        return None

    value = parse_expression(parts[1].strip(), line_number)
    if not value:
        value = parts[1].strip()

    parts = parts[0].split(":")

    type_hint = None
    if len(parts) >= 2:
        type_hint = parts[1].strip()

    name = parts[0].strip()

    return Constant(
        name=name,
        value=value,
        type_hint=type_hint,
        line_number=line_number,
    )
