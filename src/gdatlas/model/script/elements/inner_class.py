from dataclasses import dataclass, field

from .script_element import ScriptElement


@dataclass(slots=True)
class Class(ScriptElement):
    inherits: str | None = None
    elements: list[ScriptElement] = field(default_factory=list, init=False)
