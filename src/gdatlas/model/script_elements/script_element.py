from dataclasses import dataclass

@dataclass(slots=True)
class ScriptElement:
    name: str
    line_number: int