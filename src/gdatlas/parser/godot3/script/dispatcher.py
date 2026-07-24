from gdatlas.parser.common import ParseRule
from gdatlas.parser.script import (
    parse_class_name,
    parse_constant,
    parse_enum,
    parse_extends,
    parse_function,
    parse_signal,
    parse_tool,
    parse_variable,
)

PARSERS: list[ParseRule] = [
    ParseRule("static func ", parse_function),
    ParseRule("func ", parse_function),
    ParseRule("onready var ", parse_variable),
    ParseRule("export ", parse_variable),
    ParseRule("static var ", parse_variable),
    ParseRule("var ", parse_variable),
    ParseRule("const ", parse_constant),
    ParseRule("signal ", parse_signal),
    ParseRule("enum ", parse_enum),
    ParseRule("extends ", parse_extends),
    ParseRule("class_name ", parse_class_name),
    ParseRule("tool", parse_tool),
]
