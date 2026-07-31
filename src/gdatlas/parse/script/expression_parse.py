from gdatlas.model.script.expression import Load, Preload, ScriptExpression
from gdatlas.parse.tokens.godot3.script import tokens


def parse_expression(value: str, line_number: int) -> ScriptExpression | None:
    if not value:
        return None

    expression: ScriptExpression | None = None

    if value.startswith(tokens.LOAD):
        expression = _parse_load(value, line_number)
    elif value.startswith(tokens.PRELOAD):
        expression = _parse_preload(value, line_number)

    return expression


def _parse_load(value: str, line_number: int) -> Load | None:
    if not value:
        return None

    prefix = tokens.LOAD
    if not value.startswith(prefix):
        return None

    signature = value.removeprefix(prefix).strip()
    if not signature:
        return None

    path = signature.removeprefix("(").removesuffix(")").strip().strip("\"'")
    if not path:
        return None

    return Load(
        path=path,
        line_number=line_number,
    )


def _parse_preload(value: str, line_number: int) -> Preload | None:
    if not value:
        return None

    prefix = tokens.PRELOAD
    if not value.startswith(prefix):
        return None

    signature = value.removeprefix(prefix).strip()
    if not signature:
        return None

    path = signature.removeprefix("(").removesuffix(")").strip().strip("\"'")
    if not path:
        return None

    return Preload(
        path=path,
        line_number=line_number,
    )
