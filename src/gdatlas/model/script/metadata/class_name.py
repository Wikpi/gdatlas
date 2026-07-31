from dataclasses import dataclass

from .script_metadata import ScriptMetadata


@dataclass(slots=True)
class ClassName(ScriptMetadata):
    name = "class_name"
