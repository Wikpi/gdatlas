from dataclasses import dataclass

from .script_element import ScriptElement

@dataclass(slots=True)
class Metadata(ScriptElement):
    value: str | None = None