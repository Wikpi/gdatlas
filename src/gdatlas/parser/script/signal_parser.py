from gdatlas.model.script.elements import Signal
from gdatlas.parser.godot3.script import tokens

from .parameter_parser import parse_parameter


def parse_signal(line: str, line_number: int) -> Signal | None:
    if not line:
        return None

    prefix: str = f"{tokens.SIGNAL} "
    if not line.startswith(prefix):
        return None
    signature = line.removeprefix(prefix).strip()

    parts = signature.split("(", maxsplit=1)

    name = parts[0].strip()
    parameters = []

    if not name:
        return None

    if len(parts) >= 2:
        # TODO: fix paarenthesis injection bug.
        parts = parts[1].split(")")
        if len(parts) < 2:
            return None

        parameter_string = parts[0].strip()

        if parameter_string != "":
            for parameter in parts[0].strip().split(","):
                parsed_parameter = parse_parameter(parameter.strip())
                if not parsed_parameter:
                    continue

                parameters.append(parsed_parameter)

    return Signal(
        name=name,
        parameters=parameters,
        line_number=line_number,
    )
