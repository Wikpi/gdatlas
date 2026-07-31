from dataclasses import dataclass
from typing import ClassVar

from ..common import ScriptNode


@dataclass(slots=True)
class ScriptMetadata(ScriptNode):
    name: ClassVar[str]
    value: str | None = None
