from gdatlas.model.script.element import Class
from gdatlas.model.script.metadata import Extends
from gdatlas.parse.tokens.godot3.script import tokens


def parse_inner_class(line: str, line_number: int) -> Class | None:
    if not line:
        return None

    prefix: str = f"{tokens.CLASS} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).removesuffix(":").strip()

    parts = signature.split(f" {tokens.EXTENDS} ", maxsplit=1)

    metadata = []
    if len(parts) >= 2:
        value = parts[1].strip()
        if not value:
            return None

        metadata.append(
            Extends(
                value=value,
                line_number=line_number,
            )
        )

    name = parts[0].strip()
    if not name:
        return None

    return Class(
        name=name,
        metadata=metadata,
        elements=[],
        line_number=line_number,
    )
