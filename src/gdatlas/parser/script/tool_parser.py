from gdatlas.model.script.metadata import ScriptMetadata
from gdatlas.parser.godot3.script import tokens


def parse_tool(line: str, line_number: int) -> ScriptMetadata | None:
    if not line:
        return None

    prefix: str = tokens.TOOL
    if not line.startswith(prefix):
        return None

    return ScriptMetadata(
        name=tokens.TOOL,
        line_number=line_number,
    )
