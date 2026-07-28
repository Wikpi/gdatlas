from gdatlas.model.script.element import Parameter
from gdatlas.parse.tokens.godot3.script import tokens


def parse_parameter(parameter: str) -> Parameter | None:
    if not parameter:
        return None

    if parameter.startswith(f"{tokens.VARIABLE} "):
        parameter = parameter.removeprefix(f"{tokens.VARIABLE} ").strip()

    parts = parameter.split("=", maxsplit=1)

    default_value = None
    if len(parts) >= 2:
        default_value = parts[1].strip()

    parts = parts[0].split(":", maxsplit=1)

    type_hint = None
    if len(parts) >= 2:
        type_hint = parts[1].strip()

    name = parts[0].strip()

    if not name:
        return None

    return Parameter(
        name=name,
        default_value=default_value,
        type_hint=type_hint,
    )
