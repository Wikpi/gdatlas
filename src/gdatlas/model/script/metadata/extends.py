from dataclasses import dataclass, field

from .script_metadata import ScriptMetadata


@dataclass(slots=True)
class Extends(ScriptMetadata):
    name: str = field(default="extends", init=False)
