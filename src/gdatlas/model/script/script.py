from dataclasses import dataclass, field
from pathlib import Path
from typing import TypeVar

from gdatlas.model.script.elements import ScriptElement
from gdatlas.model.script.metadata import ScriptMetadata

ScriptElementType = TypeVar(
    "ScriptElementType",
    bound=ScriptElement,
)


@dataclass(slots=True)
class Script:
    path: Path

    metadata: list[ScriptMetadata] = field(default_factory=list, init=False)
    elements: list[ScriptElement] = field(default_factory=list, init=False)

    def get_elements(self, target_type: type[ScriptElementType]) -> list[ScriptElementType]:
        target_elements: list[ScriptElementType] = []

        for element in self.elements:
            if not isinstance(element, target_type):
                continue
            target_elements.append(element)

        return target_elements

    def get_metadata(self, target: str) -> ScriptMetadata | None:
        for data in self.metadata:
            if data.name != target:
                continue
            return data
        return None
