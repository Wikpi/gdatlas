from dataclasses import dataclass, field

from ..common import ScriptNode


@dataclass(slots=True)
class ScriptElement(ScriptNode):
    name: str
    documentation: str | None = field(default=None, kw_only=True)
