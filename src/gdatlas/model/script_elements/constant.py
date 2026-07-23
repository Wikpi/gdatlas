from dataclasses import dataclass

from .script_element import ScriptElement


@dataclass(slots=True)
class Constant(ScriptElement):
    value: str
    type_hint: str | None = None
