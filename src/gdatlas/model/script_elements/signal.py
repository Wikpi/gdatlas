from dataclasses import dataclass, field

from .script_element import ScriptElement

@dataclass(slots=True)
class Signal(ScriptElement):
    parameters: list[Parameter] = field(default_factory=list)