from .common import ParseRule, ParseContext

from gdatlas.model import Script
from gdatlas.model.script_elements import Function, Variable, Constant, Signal, Enum, Metadata

from gdatlas.parser.godot3.script import PARSERS as GODOT3_PARSERS

def parse_script(ctx: ParseContext, script: Script) -> None:
    # TODO: add godot version specific parser select.
    parsers = GODOT3_PARSERS
    
    with script.path.open("r") as file:
        for line_number, line in enumerate(file, start=1):
            element = _parse_line(parsers, line, line_number)

            if element is None:
                continue

            _add_element(script, element)

def _parse_line(parsers: list[ParseRule], line: str, line_number: int) -> ScriptElement | None:
    line = line.strip()
    
    for rule in parsers:
        if not line.startswith(rule.prefix):
            continue
        return rule.parser(line, line_number)
    return None

def _add_element(script: Script, element: ScriptElement) -> None:
    match element:
        case Function():
            script.functions.append(element)
        
        case Variable():
            script.variables.append(element)
        
        case Constant():
            script.constants.append(element)
        
        case Signal():
            script.signals.append(element)
        
        case Enum():
            script.enums.append(element)
        
        case Metadata():
            script.metadata.append(element)