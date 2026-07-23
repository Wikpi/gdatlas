from dataclasses import dataclass, field

from .script_element import ScriptElement
from .parameter import Parameter


@dataclass(slots=True)
class Function(ScriptElement):
    parameters: list[Parameter] = field(default_factory=list)
    return_type: str | None = None

    static: bool = False
