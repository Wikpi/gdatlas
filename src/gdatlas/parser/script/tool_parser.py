from gdatlas.model.script_elements import Metadata

def parse_tool(line: str, line_number: int) -> Metadata | None:
    prefix: str = "tool"
    if not line.startswith(prefix):
        return None
    
    return Metadata(
        name="tool",
        line_number=line_number
    )