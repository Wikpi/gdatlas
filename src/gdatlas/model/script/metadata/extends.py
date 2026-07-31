from dataclasses import dataclass

from .script_metadata import ScriptMetadata


@dataclass(slots=True)
class Extends(ScriptMetadata):
    name = "extends"
