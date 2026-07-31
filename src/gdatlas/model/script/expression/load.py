from dataclasses import dataclass
from pathlib import Path

from .script_expression import ScriptExpression


@dataclass(slots=True)
class Load(ScriptExpression):
    path: Path
    name = "load"
