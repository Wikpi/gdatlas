from gdatlas.model.script_elements import Metadata


def parse_class_name(line: str, line_number: int) -> Metadata | None:
    prefix: str = "class_name "
    if not line.startswith(prefix):
        return None

    signature = line.removeprefix(prefix).strip()

    value = signature.strip()
    if not value:
        return None

    return Metadata(
        name="class_name",
        value=value,
        line_number=line_number,
    )
