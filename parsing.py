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
    list_ = full_command.split()
    
    if (not len(list_)-1):
        for i in range(4):
            yield 0
        return

    yield len(list_)-1
    command_name = list_[0]
    print(f'Lista: {list_}')
    print(f'Lista: {list_.remove(command_name)}')
    if (list_):
        print(f'Lista: {list_}')
        for i in list_:
            print(i)
            yield i
    for i in range(expected - len(list_) - 1):
        print('ehi')
        print(expected - len(list_) - 1)
        yield 0