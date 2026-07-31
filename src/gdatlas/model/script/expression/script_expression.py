from dataclasses import dataclass
from typing import ClassVar

from gdatlas.model.script import ScriptNode


@dataclass(slots=True)
class ScriptExpression(ScriptNode):
    name: ClassVar[str]
