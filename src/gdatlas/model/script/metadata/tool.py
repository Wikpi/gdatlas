from dataclasses import dataclass

from .script_metadata import ScriptMetadata


@dataclass(slots=True)
class Tool(ScriptMetadata):
    name = "tool"
