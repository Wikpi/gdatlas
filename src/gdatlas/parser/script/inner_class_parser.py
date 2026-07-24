from gdatlas.model.script.elements import Class


def parse_inner_class(line: str, line_number: int) -> Class | None:
    prefix: str = "class "
    if not line.startswith(prefix):
        return None

    signature = line.removeprefix(prefix).removesuffix(":").strip()

    parts = signature.split(" extends ", maxsplit=1)

    inherits = None
    if len(parts) >= 2:
        inherits = parts[1].strip()
        if not inherits:
            return None

    name = parts[0].strip()
    if not name:
        return None

    return Class(
        name=name,
        inherits=inherits,
        line_number=line_number,
    )
