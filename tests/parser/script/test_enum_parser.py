import pytest

from gdatlas.parser.script import parse_enum

from gdatlas.model.script_elements import Enum, EnumMember

@pytest.mark.parametrize(
    "line, line_number, expected",
    [
        (
            "enum TestEnum { TEST_MEMBER1, TEST_MEMBER2, TEST_MEMBER3 }",
            1,
            Enum(
                name="TestEnum",
                members=[
                    EnumMember(name="TEST_MEMBER1", value=None),
                    EnumMember(name="TEST_MEMBER2", value=None),
                    EnumMember(name="TEST_MEMBER3", value=None),
                ],
                line_number=1,
            ),
        ),
        (
            "enum TestValue { TEST_MEMBER1 = 1, TEST_MEMBER2 = 0, TEST_MEMBER3 = -1 }",
            2,
            Enum(
                name="TestValue",
                members=[
                    EnumMember(name="TEST_MEMBER1", value="1"),
                    EnumMember(name="TEST_MEMBER2", value="0"),
                    EnumMember(name="TEST_MEMBER3", value="-1"),
                ],
                line_number=2,
            ),
        ),
        (
            "enum TestEmpty { }",
            3,
            Enum(
                name="TestEmpty",
                members=[],
                line_number=3,
            ),
        ),
        (
            "enum", 
            4, 
            None
        ),
        (
            "enum ", 
            5, 
            None
        ),
    ],
)
def test_parse_enum(line: str, line_number: int, expected: Enum) -> None:
    element = parse_enum(line, line_number)

    assert element == expected