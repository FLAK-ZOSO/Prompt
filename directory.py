#!/usr/bin/env Python3
from genericpath import isfile
import exceptions as e
import os
import output as o
import parsing as p
import subprocess
import variables as v


def createIf(path: str) -> bool:
    if (not os.path.exists(path)):
        os.mkdir(path)
        return True
    return False


def createFileIf(path: str) -> bool:
    if (not isfile(path)):
        with open(path, 'w'): pass
        return True
    return False


def getSupList(number: int) -> list[str]:
    if (number == 0):
        return []
    elif (number < 0):
        number = 0
    o.argument(f'Insert the ordered names of the {number} super-directories: ')
    sup: list[str] = []
    for _ in range(number):
        sup.append(o.argument('Super-directory name: '))
    print('\n\n')
    return sup


def getSubList(number: int) -> list[str]:
    if (number == 0):
        return []
    elif (number < 0):
        number = 0
    o.argument(f'Insert the names of the {number} subdrirectories: ')
    sub: list[str] = []
    for _ in range(number):
        sub.append(input('Subdirectory name: '))
    if (len(sub) - len(set(sub)) != 0):
        diff = len(sub) - len(set(sub))
        o.warn(f"There were {diff} duplicates")
        o.warn("Some subdirectories won't be created")
        sub = list(set(sub)) # Removes duplicates
    return sub


def createFull(
        path: str, name: str, 
        sup: list[str], sub: list[str]
    ) -> tuple[str, bool]:

    if (sup):
        o.system('\n\nMAKING SUPER-DIRECTORIES...\n')
        for folder in sup:
            o.system(f'Creating {path}\{folder}... ')
            if (createIf(path := f'{path}\{folder}')):
                o.done('\n')
            else:
                o.failed()
                e.FolderPermissionError(f'{path}\{folder}')

    o.system('\n\nMAKING REQUIRED FOLDER... ', end='')
    if (createIf(path := f'{path}\{name}')):
        o.done('\n')
    else:
        o.failed()
        e.FolderPermissionError(f'{path}\{name}')

    if (sub):
        o.system('\n\nMAKING SUBDIRECTORIES...\n')
        for folder in sub:
            o.system(f'Creating {path}\{folder}... ', end='')
            if (createIf(f'{path}\{folder}')):
                o.done('\n')
            else:
                o.failed()
                e.FolderPermissionError(f'{path}\{folder}')

    return (path, True)


def openFolder(path: str) -> None:
    o.system(f'Opening file explorer at {path} ')
    subprocess.Popen(rf'explorer /select, "{path}"')
    o.done('\n')


def main(full_command: str) -> None:
    _, name, dept, sub = p.command(full_command, 4)

    base_path = v.getCurrentPath()
    if (not name):
        name = o.argument('Name of the folder: ')
    if (not dept):
        dept = int(o.argument('How many subdirectories will your folder be in? '))
    if (not sub):
        sub = int(o.argument('How many subdirectories will your folder contain? '))
    dept, sub = [int(i) for i in [dept, sub]]
    if (dept or sub):
        print('\n\n')
    
    sup = getSupList(dept)
    sub = getSubList(sub)
    path, _ = createFull(base_path, name, sup, sub)
    openFolder(path)


if (__name__ == '__main__'):
    main()