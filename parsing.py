#usr/bin/env Python3
import pathlib as ptlb
import re
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


def capitalizePath(path: str) -> str:
    path = list(path)
    path[0] = path[0].upper()
    for i in range(len(path)):
        if (path[i] == '\\'):
            try:
                path[i+1] = path[i+1].upper()
            except IndexError:
                break
    return ''.join(path)


def path(path_: str) -> str:
    pattern = re.compile("^[A-Z]:\\.*$")
    if (bool(pattern.match(path_)) or memoryUnit(path_)): # Absolute path
        return capitalizePath(path_)
    return f'{v.getCurrentPath()}\{path_}' # Relative path


def memoryUnit(path: str) -> bool:
    pattern = re.compile("^[A-Z]:\\\\$")
    return bool(pattern.match(path))


def filePath(path_: str) -> str:
    if ('\\' in path_):    
        file = path_.split('\\')[-1]
        path_ = path_.removesuffix(f'\\{file}')
        path_ = path(path_)
        path_ += file
    else:
        path_ = f'{v.getCurrentPath()}\\{path_}'
    if (not path_.endswith('.txt')):
        path_ += '.txt'
    return path_