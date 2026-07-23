from dataclasses import dataclass
from typing import Callable, TypeAlias

@dataclass(slots=True)
class ParseContext:
    godot_version: str

Parser: TypeAlias = Callable[[str, int], object | None]

@dataclass(slots=True)
class ParseRule:
    prefix: str
    parser: Parser