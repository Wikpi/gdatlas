from dataclasses import dataclass


@dataclass(slots=True)
class ScriptNode:
    name: str
    line_number: int
