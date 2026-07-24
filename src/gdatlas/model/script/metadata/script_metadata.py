from dataclasses import dataclass

from ..common import ScriptNode


@dataclass(slots=True)
class ScriptMetadata(ScriptNode):
    value: str | None = None
