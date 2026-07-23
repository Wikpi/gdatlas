from dataclasses import dataclass

@dataclass(slots=True)
class Parameter:
    name: str
    default_value: str | None = None
    type_hint: str | None = None