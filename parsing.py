#!/usr/bin/env Python3
import re
from typing import Any
import variables as v


def answer(a: str) -> bool:
    if (a.lower() in ['y', 'yes']):
        return True
    elif (a.lower() not in ['n', 'no']):
        print(
            f'''Your answer ({a}) was not valid.
            This will be interpreted as a NO.\n'''
        )
    return False


def command(full_command: str, expected: int) -> (tuple[int, Any] | None):
    cmd, *args = full_command.split()
    yield cmd
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
    pattern1 = re.compile("^[A-Z]:\\.*$")
    pattern2 = re.compile("^[A-Z]:\\\\.*$")
    matches = bool(pattern1.match(path_) or pattern2.match(path_))
    if (matches or memoryUnit(path_)):
        return capitalizePath(path_) # Absolute path
    return f'{v.getCurrentPath()}\{path_}' # Relative path


def memoryUnit(path: str) -> bool:
    patterns = [
        re.compile("^[A-Z]:\\\\$"),
        re.compile("^[A-Z]:\\$"),
        re.compile("^[A-Z]:$")
    ]
    return any([pat.match(path) for pat in patterns])


def textFilePath(path_: str) -> str:
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


def removeLastFromPath(path_: str) -> str:
    path_ = path_.split('\\')
    file = path_[-1]
    return '\\'.join(path_).removesuffix(f'\\{file}')