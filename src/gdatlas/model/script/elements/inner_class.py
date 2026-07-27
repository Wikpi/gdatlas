from dataclasses import dataclass, field

from gdatlas.model.script.metadata import ScriptMetadata

from .script_element import ScriptElement


@dataclass(slots=True)
class Class(ScriptElement):
    metadata: list[ScriptMetadata] = field(default_factory=list)
    elements: list[ScriptElement] = field(default_factory=list)
