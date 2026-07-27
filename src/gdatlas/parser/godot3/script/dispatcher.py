from gdatlas.parser import script as parsers
from gdatlas.parser.common import ParseRule
from gdatlas.parser.godot3.script import tokens

PARSERS: list[ParseRule] = [
    ParseRule(f"{tokens.STATIC} {tokens.FUNCTION} ", parsers.parse_function),
    ParseRule(f"{tokens.FUNCTION} ", parsers.parse_function),
    ParseRule(f"{tokens.ONREADY} {tokens.VARIABLE} ", parsers.parse_variable),
    ParseRule(f"{tokens.EXPORT} ", parsers.parse_variable),
    ParseRule(f"{tokens.STATIC} {tokens.VARIABLE} ", parsers.parse_variable),
    ParseRule(f"{tokens.VARIABLE} ", parsers.parse_variable),
    ParseRule(f"{tokens.CONSTANT} ", parsers.parse_constant),
    ParseRule(f"{tokens.SIGNAL} ", parsers.parse_signal),
    ParseRule(f"{tokens.ENUM} ", parsers.parse_enum),
    ParseRule(f"{tokens.EXTENDS} ", parsers.parse_extends),
    ParseRule(f"{tokens.CLASS_NAME} ", parsers.parse_class_name),
    ParseRule(f"{tokens.TOOL}", parsers.parse_tool),
    ParseRule(f"{tokens.CLASS} ", parsers.parse_inner_class),
]
