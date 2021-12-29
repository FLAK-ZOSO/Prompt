#usr/bin/env Python3
import os
import subprocess
import variables as v


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
    v.incrementLine(3 + number)
    return sup


def getSubList(number: int) -> list[str]:
    print(f'Insert the names of the {number} subdrirectories: ')
    sub: list[str] = []
    for _ in range(number):
        sub.append(input('Subdirectory name: '))
    v.incrementLine(number)
    if (len(sub) - len(set(sub)) != 0):
        diff = len(sub) - len(set(sub))
        print("Some subdirectories won't be created")
        print(f"There were {diff} duplicates")
        v.incrementLine(2)
        sub = list(set(sub)) # Removes duplicates
    return sub


def createFull(
        path: str, name: str, 
        sup: list[str], sub: list[str]
    ) -> tuple[str, bool]:

    print('\n\n\nMAKING SUPER-DIRECTORIES...\n')
    v.incrementLine(4)
    for folder in sup:
        print(f'Creating {path}...', end='')
        createIf(path := f'{path}\{folder}')
        print('[DONE]')
    v.incrementLine(len(sup))

    print('\n\n\nMAKING REQUIRED FOLDER...', end='')
    createIf(path := f'{path}\{name}')
    print('[DONE]')
    v.incrementLine(3)

    print('\n\n\nMAKING SUBDIRECTORIES...\n')
    v.incrementLine(4)
    for folder in sub:
        print(f'Creating {path}\{folder}...', end='')
        createIf(f'{path}\{folder}')
        print('[DONE]')
    v.incrementLine(len(sub))

    return (path, True)


def openFolder(path: str) -> None:
    subprocess.Popen(rf'explorer /select, "{path}"')


def main() -> None:
    base_path = v.getCurrentPath()
    name = input('Name of the folder: ')
    dept = int(input('How many subdirectories will your folder be in? '))
    sub = int(input('How many subdirectories will your folder contain? '))
    print('\n\n')
    v.incrementLine(5)
    
    sup = getSupList(dept)
    sub = getSubList(sub)
    path, worked = createFull(base_path, name, sup, sub)
    openFolder(path)


if (__name__ == '__main__'):
    main()