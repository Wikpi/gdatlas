from dataclasses import dataclass
from pathlib import Path

@dataclass
class Script:
    path: Path

    def __init__(self, path: Path) -> None:
        self.path = path