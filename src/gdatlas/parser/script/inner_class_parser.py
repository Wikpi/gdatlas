from gdatlas.model.script.elements import Class
from gdatlas.parser.godot3.script import tokens


def parse_inner_class(line: str, line_number: int) -> Class | None:
    if not line:
        return None

    prefix: str = f"{tokens.CLASS} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).removesuffix(":").strip()

    parts = signature.split(f" {tokens.EXTENDS} ", maxsplit=1)

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
