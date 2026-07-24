from gdatlas.model.script.elements import Function

from .parameter_parser import parse_parameter


def parse_function(line: str, line_number: int) -> Function | None:
    is_static = False
    if line.startswith("static "):
        line = line.removeprefix("static ")
        is_static = True

    prefix: str = "func "
    if not line.startswith(prefix):
        return None

    signature = line.removeprefix(prefix).strip()

    parts = signature.split("(", maxsplit=1)
    if len(parts) < 2:
        return None

    name = parts[0].strip()

    # TODO: fix string injection bug.
    parts = parts[1].split(")")
    if len(parts) < 2:
        return

    parameters = []

    parameter_string = parts[0].strip()

    if parameter_string != "":
        for parameter in parameter_string.split(","):
            parsed_parameter = parse_parameter(parameter.strip())
            if not parsed_parameter:
                continue

            parameters.append(parsed_parameter)

    return_type = None
    if parts[1].strip().startswith("->"):
        return_type = parts[1].strip().removeprefix("->").strip().removesuffix(":").strip()

    return Function(
        name=name,
        parameters=parameters,
        return_type=return_type,
        line_number=line_number,
        static=is_static,
    )
