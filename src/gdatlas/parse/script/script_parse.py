from gdatlas.model.script import Script, ScriptNode
from gdatlas.model.script.element import Class, ScriptElement
from gdatlas.model.script.metadata import ScriptMetadata
from gdatlas.parse.common import ParseContext, ParseRule

from .dispatch import PARSERS as GODOT3_PARSERS


def parse_script(ctx: ParseContext, script: Script) -> None:
    # TODO: add godot version specific parser select.
    parsers = GODOT3_PARSERS

    scope_stack: list[Script | Class] = [script]

    with script.path.open("r") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            while _get_scope_level(line) < (len(scope_stack) - 1):
                scope_stack.pop()

            node = _parse_line(parsers, line, line_number)
            if not node:
                continue

            scope = scope_stack[-1]

            _add_node(scope, node)

            if not isinstance(node, Class):
                continue
            scope_stack.append(node)


def _get_scope_level(line: str) -> int:
    return len(line) - len(line.lstrip("\t"))


def _parse_line(parsers: list[ParseRule], line: str, line_number: int) -> ScriptNode | None:
    line = line.strip()

    for rule in parsers:
        if not line.startswith(rule.prefix):
            continue
        return rule.parser(line, line_number)
    return None


def _add_node(scope: Script | Class, node: ScriptNode) -> None:
    match node:
        case ScriptElement():
            scope.elements.append(node)

        case ScriptMetadata():
            scope.metadata.append(node)
