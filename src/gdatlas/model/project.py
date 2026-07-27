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

    def find_script(self, path: Path) -> Script | None:
        for script in self.scripts:
            if script.path == path:
                return script
        return None
