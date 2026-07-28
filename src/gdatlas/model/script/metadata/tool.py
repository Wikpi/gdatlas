from dataclasses import dataclass, field

from .script_metadata import ScriptMetadata


@dataclass(slots=True)
class Tool(ScriptMetadata):
    name: str = field(default="tool", init=False)
