from dataclasses import dataclass, field
from pathlib import Path

from .scene import Scene
from .script import Script


@dataclass(slots=True)
class Project:
    path: Path

    godot_version: str

    scripts: list[Script] = field(default_factory=list)
    scenes: list[Scene] = field(default_factory=list)
