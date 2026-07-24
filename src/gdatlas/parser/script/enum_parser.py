from gdatlas.model.script.elements import Enum, EnumMember


def parse_enum(line: str, line_number: int) -> Enum | None:
    signature = line.removeprefix("enum ").strip()

    parts = signature.split("{", maxsplit=1)
    if len(parts) < 2:
        return None

    name = parts[0].strip()
    members = []

    for member in parts[1].removesuffix("}").strip().split(","):
        parsed_member = _parse_member(member.strip())
        if not parsed_member:
            continue

        members.append(parsed_member)

    return Enum(
        name=name,
        members=members,
        line_number=line_number,
    )


def _parse_member(member: str) -> EnumMember | None:
    if not member:
        return None

    parts = member.split("=", maxsplit=1)

    name = parts[0].strip()
    value = None

    if not name:
        return None

    if len(parts) >= 2:
        value = parts[1].strip()

    return EnumMember(
        name=name,
        value=value,
    )
