from dataclasses import dataclass


@dataclass(slots=True)
class ScriptNode:
    line_number: int
