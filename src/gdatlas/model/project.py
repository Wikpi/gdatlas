from dataclasses import dataclass, field
from pathlib import Path

from .script import Script
from .scene import Scene


@dataclass(slots=True)
class Project:
    path: Path

    godot_version: str

    scripts: list[Script] = field(default_factory=list)
    scenes: list[Scene] = field(default_factory=list)
