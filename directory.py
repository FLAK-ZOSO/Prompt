#usr/bin/env Python3
import os
import subprocess


def createIf(path: str) -> bool:
    if (not os.path.exists(path)):
        os.mkdir(path)
        return True
    return False


def getSupList(number: int) -> list[str]:
    print(f'Insert the ordered names of the {number} super-directories: ')
    sup: list[str] = []
    for _ in range(number):
        sup.append(input('Super-directory name: '))
    print('\n\n')
    return sup


def getSubList(number: int) -> list[str]:
    print(f'Insert the names of the {number} subdrirectories: ')
    sub: list[str] = []
    for _ in range(number):
        sub.append(input('Subdirectory name: '))
    if (len(sub) - len(set(sub)) != 0):
        diff = len(sub) - len(set(sub))
        print("Some subdirectories won't be created")
        print(f"There were {diff} duplicates")
        sub = list(set(sub)) # Removes duplicates
    return sub


def createFull(path: str, name: str, sup: list[str], sub: list[str]) -> tuple:

    print('\n\n\nMAKING SUPER-DIRECTORIES...\n')
    for folder in sup:
        print(f'Creating {path}...', end='')
        createIf(path := f'{path}\{folder}')
        print('[DONE]')

    print('\n\n\nMAKING REQUIRED FOLDER...', end='')
    createIf(path := f'{path}\{name}')
    print('[DONE]')

    print('\n\n\nMAKING SUBDIRECTORIES...\n')
    for folder in sub:
        print(f'Creating {path}\{folder}...', end='')
        createIf(f'{path}\{folder}')
        print('[DONE]')

    return (path, True)


def open(path: str) -> None:
    subprocess.Popen(rf'explorer "{path}"')