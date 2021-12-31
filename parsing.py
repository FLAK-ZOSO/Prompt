#usr/bin/env Python3
from typing import Any
import variables as v


def answer(a: str) -> bool:
    if (a.lower() in ['y', 'yes']):
        return True
    elif (a.lower() in ['n', 'no']):
        return False
    else:
        print(
            f'''Your answer ({a}) was not valid.
            This will be interpreted as a NO.\n'''
        )
        v.incrementLine(3)
        return False


def command(full_command: str, expected: int) -> (tuple[int, Any] | None):
    _, *args = full_command.split()
    yield len(args)
    yield from args
    for _ in range(expected - len(args) - 1):
        yield False