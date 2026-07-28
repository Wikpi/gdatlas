from gdatlas.model.script.metadata import Tool
from gdatlas.parse.tokens.godot3.script import tokens


def parse_tool(line: str, line_number: int) -> Tool | None:
    if not line:
        return None

    prefix: str = tokens.TOOL
    if not line.startswith(prefix):
        return None

    return Tool(
        line_number=line_number,
    )
