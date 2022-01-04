#!/usr/bin/env Python3
import directory as d
import exceptions as e
import json
import os
import parsing as p
import shutil as sh
import source as s
import variables as v


def changePath(full_command: str) -> bool:
    try: #EAFP
        new = full_command.split()[1]
    except IndexError:
        new = input('Specify a value for missing parameter (path): ')
    new = p.path(new)
    print(f'Checking the existence of {new}... ', end='')
    if (not os.path.exists(new)):
        print('[FAILED]')
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
        v.customPathAsCurrent(new)
    return True


def close(current_path: str) -> None:
    if (current_path == v.getDefaultPath()):
        return
    print(
        f'Do you want to have back {current_path} instead of {v.getDefaultPath()}' 
        ' as your path for the next run? (y/n)'
    )
    if (p.answer(input('> '))):
        v.currentPathAsDefault()
    else:
        print(f'The default path will remain {v.getDefaultPath()}')


def promptHelp(full_command: str=None) -> None:
    _, command = p.command(full_command, 2)
    if (not command):
        command = 'help'
    command = command.lower()
    if (command not in commands.keys()):
        print(f'[ABORTED] {command} is not an existing command')
        return
    if (os.path.exists(f'help/{command}.txt')):
        with open(f'help/{command}.txt', 'r') as file:
            print(file.read())
    else:
        with open(f'help/{synonims[command]}.txt', 'r') as file:
            print(file.read())


def setVar(full_command: str) -> None:
    _, var, val, typ = p.command(full_command, 4)
    if (not var):
        var = input('Name of your variable: ')
    if (not val):
        val = input('Value of your variable: ')
    if (not typ):
        typ = input('Type of your variable: ')
    
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
                    val = True
        val = v.types[typ.lower()](val)
    else:
        print(f'Type {typ} not found')
        typ = 'str'
        val = str(val) # It was already a string
        print('Type was set to default value: str')

    path = f'var/{var}.json'
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
        print(f'Changed {before} to {val} in {path}')
    else:
        print(f'[WARNING] the requested variable was empty.')
        print(f'Opening {path} in write mode... ', end='')
        with open(path, 'w') as variable:
            print('[DONE]')
            json.dump(val, variable)
            print(f'Closing {path}... ', end='')
        print('[DONE]')


def echo(full_command: str) -> None:
    print(full_command.removeprefix('echo '))


def run(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    if (not path):
        path = input('Specify a value for missing argument (path): ')
    path = p.path(path)
    if (not path.endswith('.txt')):
        path += '.txt'
    print(f'Checking the existence of {path}... ', end='')
    if (not os.path.exists(path)):
        print('[DONE] [FALSE]')
        e.DirectoryException(path)
        return
    else:
        print('[DONE] [TRUE]')
    s.run(path)


def makeFile(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    path = p.textFilePath(path)
    print(f'Checking the existence of {path}... ', end='')
    if (d.createFileIf(path)):
        print('[DONE] [FALSE]')
    else:
        print('[DONE] [TRUE]')
        print(f'[WARNING] {path} was already existing')


def makeSource(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    if (not path):
        path = input('Insert missing argument (file-name): ')

    makeFile(f'make {path}')
    path = p.textFilePath(path)
    print(f'Opening {path} in append mode... ', end='')
    with open(path, 'a') as target:
        print('[DONE]')
        for i in range(200): # 200 is the maximum of lines
            line = input(f'{i}: ')
            if (not line): # An empty line ends the command
                target.write('\n')
                break
            target.write(f'{line}\n')
        print(f'Closing {path}... ', end='')
    print('[DONE]')


def makeDirectory(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    if (not path):
        path = input('Insert missing argument (path): ')
    path = p.path(path)
    print(f'Checking if {path} exists... ', end='')
    if (d.createIf(path)):
        print(f'[DONE] [FALSE]')
        print(f'Creating {path}... [DONE]')
    else:
        print('[DONE] [TRUE]')


def cleanScreen(full_command=None) -> None:
    for _ in range(4):
        print('\n' * 10)


def moveFolder(full_command: str) -> None:
    _, f, new = p.command(full_command, 3)
    f = f if f else input('Insert missing argument (file/folder): ')
    new = new if new else input('Insert missing argument (new-path): ')

    f_ = p.path(f)
    if (os.path.exists(new)):
        new = p.path(new)
    else:
        e.DirectoryException(new)
        return

    if (os.path.exists(f_)):
        des = f'{new}\\{f}'
        des_ = p.removeLastFromPath(des)
        print(f'Creating {des}... [DONE]') if d.createIf(des_) else None
        print(f'Moving everything to {des}... ', end='')
        sh.move(f_, des)
        print('[DONE]')
    else:
        e.DirectoryException(f_)


def loop(full_command: str) -> None:
    _, repetitions, path = p.command(full_command, 3)
    try:
        [run(f'run {path}') for _ in range(int(repetitions))]
    except RecursionError:
        print(f'[ABORT] Too many recursive calls occurred')


commands = {
    'cd': changePath,
    'cls': cleanScreen,
    'directory': d.main, # Complex command stored in module directory
    'echo': echo,
    'help': promptHelp,
    'loop': loop,
    'makedir': makeDirectory,
    'makefile': makeFile,
    'makesource': makeSource,
    'move': moveFolder,
    'path': changePath,
    'run': run,
    'setvar': setVar,
    'source': makeSource,
    '@': setVar
}


synonims = {
    'cd': 'path',
    'end': 'close',
    'exit': 'close',
    'quit': 'close',
    'makesource': 'source',
    '@': 'setvar',
}