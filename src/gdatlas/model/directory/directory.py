from dataclasses import dataclass, field
from pathlib import Path

from gdatlas.model.script import Script


@dataclass(slots=True)
class Directory:
    path: Path
    directories: dict[str, "Directory"] = field(default_factory=dict)
    scripts: list[Script] = field(default_factory=list)
