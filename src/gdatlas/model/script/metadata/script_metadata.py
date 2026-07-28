from dataclasses import dataclass

from ..common import ScriptNode


@dataclass(slots=True)
class ScriptMetadata(ScriptNode):
    name: str
    value: str | None = None
