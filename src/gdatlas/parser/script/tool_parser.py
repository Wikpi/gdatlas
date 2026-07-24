from gdatlas.model.script.metadata import ScriptMetadata


def parse_tool(line: str, line_number: int) -> ScriptMetadata | None:
    prefix: str = "tool"
    if not line.startswith(prefix):
        return None

    return ScriptMetadata(
        name="tool",
        line_number=line_number,
    )
