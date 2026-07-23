from gdatlas.model.script_elements import Variable


def parse_variable(line: str, line_number: int) -> Variable | None:
    is_onready = False
    is_export = False
    is_static = False

    while True:
        if line.startswith("onready "):
            if is_onready:
                return None

            line = line.removeprefix("onready ").strip()
            is_onready = True

        elif line.startswith("export "):
            if is_export:
                return None

            line = line.removeprefix("export ").strip()
            is_export = True

        elif line.startswith("static "):
            if is_static:
                return None

            line = line.removeprefix("static ").strip()
            is_static = True

        else:
            break

    prefix: str = "var "
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
