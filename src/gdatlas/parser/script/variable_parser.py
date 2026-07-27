from gdatlas.model.script.elements import Variable
from gdatlas.parser.godot3.script import tokens


def parse_variable(line: str, line_number: int) -> Variable | None:
    if not line:
        return None

    line, is_onready, is_export, is_static = _get_modifiets(line)

    prefix: str = f"{tokens.VARIABLE} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).strip()

    parts = signature.split("=", maxsplit=1)

    value = None
    if len(parts) >= 2:
        value = parts[1].strip()

    parts = parts[0].split(":", maxsplit=1)

    type_hint = None
    if len(parts) >= 2:
        type_hint = parts[1].strip()

    name = parts[0].strip()
    if not name:
        return None

    return Variable(
        name=name,
        default_value=value,
        type_hint=type_hint,
        static=is_static,
        export=is_export,
        onready=is_onready,
        line_number=line_number,
    )


def _get_modifiets(line: str) -> tuple[str, bool, bool, bool]:
    is_onready = False
    is_export = False
    is_static = False

    while True:
        if line.startswith(f"{tokens.ONREADY} "):
            if is_onready:
                return None

            line = line.removeprefix(f"{tokens.ONREADY} ").strip()
            is_onready = True

        elif line.startswith(f"{tokens.EXPORT} "):
            if is_export:
                return None

            line = line.removeprefix(f"{tokens.EXPORT} ").strip()
            is_export = True

        elif line.startswith(f"{tokens.STATIC} "):
            if is_static:
                return None

            line = line.removeprefix(f"{tokens.STATIC} ").strip()
            is_static = True

        else:
            break

    return line, is_onready, is_export, is_static
