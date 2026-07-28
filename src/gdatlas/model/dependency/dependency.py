from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdatlas.model.script import Script, ScriptNode


@dataclass(slots=True)
class Dependency:
    target: Script
    source: ScriptNode
