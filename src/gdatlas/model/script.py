from dataclasses import dataclass, field
from pathlib import Path

from gdatlas.model.script_elements import (
    Constant,
    Enum,
    Function,
    Metadata,
    Signal,
    Variable,
)


@dataclass(slots=True)
class Script:
    path: Path

    functions: list[Function] = field(default_factory=list, init=False)
    variables: list[Variable] = field(default_factory=list, init=False)
    constants: list[Constant] = field(default_factory=list, init=False)
    signals: list[Signal] = field(default_factory=list, init=False)
    enums: list[Enum] = field(default_factory=list, init=False)
    metadata: list[Metadata] = field(default_factory=list, init=False)
