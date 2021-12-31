#usr/bin/env Python3
import parsing as p
import variables as v


def changePath(full_command: str) -> None:
    try: #EAFP
        new = full_command.split()[1]
    except IndexError:
        new = input('Specify a value for missing parameter (path): ')
    print(f'Checking {new} path... ', end='')
    if (new == v.getCurrentPath()):
        print('[DONE]')
        print(f'The {new} path was already selected. No action was performed.')
    else:
        print('[DONE]')
        print(f'Selecting {new}... ', end='')
        v.customPathAsCurrent(new)
    v.incrementLine(2)


def close(current_path: str) -> None:
    if (current_path == v.getDefaultPath()):
        return
    print(
        f'Do you want to have back {current_path} instead of {v.getDefaultPath()}' 
        ' as your path for the next run? (y/n)'
    )
    if (p.answer(input(f'{v.getLine()}: >'))):
        v.currentPathAsDefault()
    else:
        print(f'The default path will remain {v.getDefaultPath()}')
    v.incrementLine(1)


def promptHelp(full_command: str=None) -> None:
    with open('help.txt', 'r') as file:
        print(content := file.read())
    content = content.count('\n')
    v.incrementLine(content)