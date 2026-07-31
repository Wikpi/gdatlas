from dataclasses import dataclass
from pathlib import Path

from .script_expression import ScriptExpression


@dataclass(slots=True)
class Preload(ScriptExpression):
    path: Path
    name = "preload"
