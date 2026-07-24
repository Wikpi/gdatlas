from dataclasses import dataclass, field
from pathlib import Path

from gdatlas.model.script.elements import ScriptElement
from gdatlas.model.script.metadata import ScriptMetadata


@dataclass(slots=True)
class Script:
    path: Path

    metadata: list[ScriptMetadata] = field(default_factory=list, init=False)
    elements: list[ScriptElement] = field(default_factory=list, init=False)
