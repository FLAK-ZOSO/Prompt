#usr/bin/env Python3
import directory as d
import exceptions as e
import json
import os
import parsing as p
import source as s
import variables as v


def changePath(full_command: str) -> (bool | None):
    try: #EAFP
        new = full_command.split()[1]
    except IndexError:
        new = input('Specify a value for missing parameter (path): ')
    new = p.path(new)
    print(f'Checking the existence of {new}... ', end='')
    if (not os.path.exists(new)):
        print('[FAILED]')
        v.incrementLine(2)
        return False
    print('[DONE]')
    print(f'Checking if {new} and {v.getCurrentPath()} are different... ', end='')
    if (new.upper() == v.getCurrentPath().upper() 
        or new.upper() == v.getCurrentPath().upper().removesuffix('\\')):
        print('[DONE] [TRUE]')
        print(f'The {new} path was already selected. No action was performed.')
    else:
        print('[DONE] [FALSE]')
        print(f'Selecting {new}... ')
        v.customPathAsCurrent(new, v.getVerbose())
    v.incrementLine(3)


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


def setVar(full_command: str) -> None:
    _, var, val, typ = p.command(full_command, 4)
    if (not var):
        var = input('Name of your variable: ')
        v.incrementLine(1)
    if (not val):
        val = input('Value of your variable: ')
        v.incrementLine(1)
    if (not typ):
        typ = input('Type of your variable: ')
        v.incrementLine(1)
    
    if (typ.lower() in v.types.keys()):
        if (typ.lower() == 'bool'):
            match (val.lower()):
                case 'true':
                    val = True
                case 'false':
                    val = False
                case _:
                    print(f'{val} cannot be interpreted as a boolean.')
                    print('Value was set to default value: True')
                    v.incrementLine(2)
                    val = True
        val = v.types[typ.lower()](val)
    else:
        print(f'Type {typ} not found')
        typ = 'str'
        val = str(val) # It was already a string
        print('Type was set to default value: str')
        v.incrementLine(2)

    path = f'{var}.json'
    if (os.path.exists(path)):
        print(f'Opening {path} in read mode... ', end='')
        with open(path, 'r') as variable:
            print('[DONE]')
            before = json.load(variable)
            print(f'Closing {path}... ', end='')
        print('[DONE]')
        print(f'Opening {path} in write mode... ', end='')
        with open(path, 'w') as variable:
            print('[DONE]')
            json.dump(val, variable)
            print(f'Closing {path}... ', end='')
        print('[DONE]')
        v.incrementLine(4)
        print(f'Changed {before} to {val} in {path}')
    else:
        print(f'[WARNING]: the requested variable was empty.')
        print(f'Opening {path} in write mode... ', end='')
        with open(path, 'w') as variable:
            print('[DONE]')
            json.dump(val, variable)
            print(f'Closing {path}... ', end='')
        print('[DONE]')
        v.incrementLine(3)


def echo(full_command: str) -> None:
    print(full_command.removeprefix('echo '))
    v.incrementLine(1 + full_command.count('\n'))


def run(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    if (not path):
        path = input('Specify a value for missing argument (path): ')
        v.incrementLine(1)
    path = p.path(path)
    if (not path.endswith('.txt')):
        path += '.txt'
    print(f'Checking the existence of {path}... ', end='')
    if (not os.path.exists(path)):
        print('[DONE] [FALSE]')
        v.incrementLine(1)
        e.DirectoryException(path)
        return
    else:
        print('[DONE] [TRUE]')
        v.incrementLine(1)
    s.run(path)


def makeFile(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    path = p.filePath(path)
    print(f'Checking the existence of {path}... ', end='')
    if (d.createFileIf(path)):
        print('[DONE] [FALSE]')
        v.incrementLine(1)
    else:
        print('[DONE] [TRUE]')
        print(f'[WARNING] {path} was already existing')
        v.incrementLine(2)


commands = {
    'cd': changePath,
    'make': makeFile,
    'directory': d.main, # Complex command stored in module directory
    'echo': echo,
    'help': promptHelp,
    'path': changePath,
    'run': run,
    'setvar': setVar,
    '@': setVar
}