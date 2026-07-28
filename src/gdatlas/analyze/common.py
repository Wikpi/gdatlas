from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from gdatlas.model import Project
from gdatlas.model.script import Script, ScriptNode


@dataclass(slots=True)
class AnalyzeContext:
    project: Project

    def resolve_script_reference(self, reference: str | Path) -> Script | None:
        if not self.project or not reference:
            return None

        if isinstance(reference, Path):
            return self.project.find_script_by_path(reference)

        if reference.startswith("res://"):
            return self.project.find_script_by_path(Path(reference))

        return self.project.find_script_by_class(reference)


@dataclass(slots=True)
class AnalyzeRule:
    token: str
    analyzer: Callable[AnalyzeContext, ScriptNode]
