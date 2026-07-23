from dataclasses import dataclass

from .script_element import ScriptElement

@dataclass(slots=True)
class Variable(ScriptElement):
    default_value: str | None = None
    type_hint: str | None = None

    static: bool = False
    export: bool = False
    onready: bool = False
    const: bool = False