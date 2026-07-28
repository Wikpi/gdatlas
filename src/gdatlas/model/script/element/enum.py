from dataclasses import dataclass, field

from .script_element import ScriptElement


@dataclass(slots=True)
class EnumMember:
    name: str
    value: int | None = None


@dataclass(slots=True)
class Enum(ScriptElement):
    members: list[EnumMember] = field(default_factory=list)
