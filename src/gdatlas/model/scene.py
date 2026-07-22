from dataclasses import dataclass
from pathlib import Path


@dataclass
class Scene:
    path: Path

    def __init__(self, path: Path) -> None:
        self.path = path
