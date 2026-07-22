from dataclasses import dataclass
from pathlib import Path

from .script import Script
from .scene import Scene

@dataclass
class Project:
    path: Path
    scripts: list[Script]
    scenes: list[Scene]

    def __init__(self, path: Path, scripts: list[Script], scenes: list[Scene]) -> None:
        self.path = path
        self.scripts = scripts
        self.scenes = scenes