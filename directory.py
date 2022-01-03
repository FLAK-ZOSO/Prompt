#!/usr/bin/env Python3
from genericpath import isfile
import exceptions as e
import os
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
    print(f'Insert the ordered names of the {number} super-directories: ')
    sup: list[str] = []
    for _ in range(number):
        sup.append(input('Super-directory name: '))
    print('\n\n')
    v.incrementLine(1 + number + 2)
    return sup


def getSubList(number: int) -> list[str]:
    if (number == 0):
        return []
    elif (number < 0):
        number = 0
    print(f'Insert the names of the {number} subdrirectories: ')
    sub: list[str] = []
    for _ in range(number):
        sub.append(input('Subdirectory name: '))
    if (len(sub) - len(set(sub)) != 0):
        diff = len(sub) - len(set(sub))
        print("Some subdirectories won't be created")
        print(f"There were {diff} duplicates")
        sub = list(set(sub)) # Removes duplicates
        v.incrementLine(2)
    v.incrementLine(1 + number)
    return sub


def createFull(
        path: str, name: str, 
        sup: list[str], sub: list[str]
    ) -> tuple[str, bool]:

    if (sup):
        print('\n\nMAKING SUPER-DIRECTORIES...\n')
        for folder in sup:
            print(f'Creating {path}\{folder}... ', end='')
            if (createIf(path := f'{path}\{folder}')):
                print('[DONE]')
            else:
                print('[FAILED]')
                e.FolderPermissionError(f'{path}\{folder}')
        v.incrementLine(4 + len(sup))

    print('\n\nMAKING REQUIRED FOLDER... ', end='')
    if (createIf(path := f'{path}\{name}')):
        print('[DONE]')
    else:
        print('[FAILED]')
        e.FolderPermissionError(f'{path}\{name}')
    v.incrementLine(3)

    if (sub):
        print('\n\nMAKING SUBDIRECTORIES...\n')
        for folder in sub:
            print(f'Creating {path}\{folder}... ', end='')
            if (createIf(f'{path}\{folder}')):
                print('[DONE]')
            else:
                print('[FAILED]')
                e.FolderPermissionError(f'{path}\{folder}')
        v.incrementLine(4 + len(sub))

    return (path, True)


def openFolder(path: str) -> None:
    print(f'Opening file explorer at {path} ', end='')
    subprocess.Popen(rf'explorer /select, "{path}"')
    print('[DONE]')


def main(full_command: str) -> None:
    _, name, dept, sub = p.command(full_command, 4)

    base_path = v.getCurrentPath()
    if (not name):
        name = input('Name of the folder: ')
        v.incrementLine(1)
    if (not dept):
        dept = int(input('How many subdirectories will your folder be in? '))
        v.incrementLine(1)
    if (not sub):
        sub = int(input('How many subdirectories will your folder contain? '))
        v.incrementLine(1)
    dept, sub = [int(i) for i in [dept, sub]]

    if (dept or sub):
        print('\n\n')
        v.incrementLine(2)
    
    sup = getSupList(dept)
    sub = getSubList(sub)
    path, _ = createFull(base_path, name, sup, sub)
    openFolder(path)


if (__name__ == '__main__'):
    main()