from gdatlas.parse.common import ParseRule
from gdatlas.parse.tokens.godot3.script import tokens

from .class_name_parse import parse_class_name
from .constant_parse import parse_constant
from .enum_parse import parse_enum
from .extends_parse import parse_extends
from .function_parse import parse_function
from .inner_class_parse import parse_inner_class
from .signal_parse import parse_signal
from .tool_parse import parse_tool
from .variable_parse import parse_variable

PARSERS: list[ParseRule] = [
    ParseRule(f"{tokens.STATIC} {tokens.FUNCTION} ", parse_function),
    ParseRule(f"{tokens.FUNCTION} ", parse_function),
    ParseRule(f"{tokens.ONREADY} {tokens.VARIABLE} ", parse_variable),
    ParseRule(f"{tokens.EXPORT} ", parse_variable),
    ParseRule(f"{tokens.STATIC} {tokens.VARIABLE} ", parse_variable),
    ParseRule(f"{tokens.VARIABLE} ", parse_variable),
    ParseRule(f"{tokens.CONSTANT} ", parse_constant),
    ParseRule(f"{tokens.SIGNAL} ", parse_signal),
    ParseRule(f"{tokens.ENUM} ", parse_enum),
    ParseRule(f"{tokens.EXTENDS} ", parse_extends),
    ParseRule(f"{tokens.CLASS_NAME} ", parse_class_name),
    ParseRule(f"{tokens.TOOL}", parse_tool),
    ParseRule(f"{tokens.CLASS} ", parse_inner_class),
]
