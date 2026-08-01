import sys

from .dispatch import COMMANDS


def main() -> None:
    command = COMMANDS[sys.argv[1]]

    command(sys.argv[2])
