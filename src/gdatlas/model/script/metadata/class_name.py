from dataclasses import dataclass, field

from .script_metadata import ScriptMetadata


@dataclass(slots=True)
class ClassName(ScriptMetadata):
    name: str = field(default="class_name", init=False)
