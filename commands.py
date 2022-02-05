#!/usr/bin/env Python3
import directory as d
import exceptions as e
import json
import os
import output as o
import parsing as p
import shutil as sh
import source as s
import variables as v


def changePath(full_command: str) -> bool:
    try: #EAFP
        new = full_command.split()[1]
    except IndexError:
        new = o.argument('Specify a value for missing argument (path): ')
    new = p.path(new)
    o.system(f'Checking the existence of {new}... ')
    if (not os.path.exists(new)):
        o.failed()
        return False
    o.done('\n')
    o.system(f'Checking if {new} and {v.getCurrentPath()} are different... ')
    if (new.upper() == v.getCurrentPath().upper() 
        or new.upper() == v.getCurrentPath().upper().removesuffix('\\')):
        o.done()
        o.true()
        o.system(f'The {new} path was already selected. No action was performed.', '\n')
    else:
        o.done()
        o.false()
        o.system(f'Selecting {new}... ', '\n')
        v.customPathAsCurrent(new)
    return True


def close(full_command: str=None) -> None:
    current = v.getCurrentPath()
    default = v.getDefaultPath()
    if (current == default):
        return
    o.question(
        f'Do you want to have back {current} instead of {default}' 
        ' as your path for the next run? (y/n)'
    )
    if (p.answer(o.question('> '))):
        v.currentPathAsDefault()
    else:
        o.system(f'The default path will remain {default}')


def promptHelp(full_command: str=None) -> None:
    _, command = p.command(full_command, 2)
    if (not command):
        command = 'help'
    command = command.lower()
    if (command not in commands.keys() and command not in synonims.keys()):
        o.abort(f'{command} is not an existing command')
        return
    if (os.path.exists(f'help/{command}.txt')):
        with open(f'help/{command}.txt', 'r') as file:
            print(file.read())
        return
    try:
        with open(f'help/{synonims[command]}.txt', 'r') as file:
            print(file.read())
    except KeyError:
        o.abort(f'Command {command} exists, but its usage instruction weren\'t provided.')


def setVar(full_command: str) -> None:
    _, var, val, typ = p.command(full_command, 4)
    var = var if var else o.argument('Name of your variable: ')
    val = val if val else o.argument('Value of your variable: ')
    typ = typ if typ else o.argument('Type of your variable: ')
        
    if (var.isspace() or not var):
        o.abort('No given variable')
        return
    if (val.isspace() or not val):
        o.warn(f'No given value')
        o.system('Value was set to default value: None')
        val = 'None'
    o.variable(val, 'value')
    
    if (typ.lower() in v.types.keys()):
        if (typ.lower() == 'bool'):
            match (val.lower()):
                case 'true' | 'on':
                    val = True
                case 'false' | 'off':
                    val = False
                case _:
                    o.warn(f'{val} cannot be interpreted as a boolean.')
                    o.system('Value was set to default value: True')
                    val = True
        val = v.types[typ.lower()](val)
    else:
        if (typ.isspace() or not typ):
            o.warn(f'No given type')
        else:
            o.warn(f'Type {typ} not found')
        typ = 'str'
        o.system('Type was set to default value: str')
        o.done('\n')

    path = f'var/{var}.json'
    if (os.path.exists(path)):
        o.system(f'Opening {path} in read mode... ')
        with open(path, 'r') as variable:
            o.done('\n')
            before = json.load(variable)
            o.system(f'Closing {path}... ')
        o.done('\n')
        o.system(f'Opening {path} in write mode...')
        with open(path, 'w') as variable:
            o.done('\n')
            json.dump(val, variable)
            o.system(f'Closing {path}...')
        o.done('\n')
        o.system(f'Changed {before} to {val} in {path}')
        o.done('\n')
    else:
        o.warn(f'The requested variable was empty.')
        o.system(f'Opening {path} in write mode... ')
        with open(path, 'w') as variable:
            o.done('\n')
            json.dump(val, variable)
            o.system(f'Closing {path}... ')
        o.done('\n')
    o.variable(val, var)


def echo(full_command: str) -> None:
    print(' '.join(full_command.split()[1:]))


def run(full_command: str) -> bool:
    _, path = p.command(full_command, 2)
    if (not path):
        path = o.argument('Specify a value for missing argument (path): ')
    if (path.isspace() or not path):
        o.error('No path was provided')
        o.abort('Command ended without executing any file')
        return False
    path = p.path(path)
    if (not path.endswith('.txt')):
        path += '.txt'
    o.system(f'Checking the existence of {path}... ')
    if (not os.path.exists(path)):
        o.done()
        o.false()
        e.DirectoryException(path)
        return False
    else:
        o.done()
        o.true()
    return s.run(path)


def makeFile(full_command: str) -> bool:
    _, path = p.command(full_command, 2)
    path = path if path else o.argument('Specify a value for missing argument (path): ')
    if (path.isspace() or not path):
        o.error('No path was provided')
        o.abort('Command ended without creating any file')
        return False
    path = p.textFilePath(path)
    o.system(f'Checking the existence of {path}... ')
    try:
        if (d.createFileIf(path)):
            o.done()
            o.false()
        else:
            o.done()
            o.true()
            o.warn(f'{path} was already existing')
        return True
    except PermissionError:
        print('\n')
        e.PromptPermissionError(f'{path} can\'t be created')
        o.abort(f'Command ended without creating any file')
        return False


def makeSource(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    if (not path):
        path: str = o.argument('Insert missing argument (file-name): ')
    if (path.isspace() or not path):
        o.abort('No given file name')
        return

    if (not makeFile(f'make {path}')):
        return
    path = p.textFilePath(path)
    o.system(f'Opening {path} in append mode... ')
    with open(path, 'a') as target:
        o.done('\n')
        for i in range(200): # 200 is the maximum of lines
            line = input(f'{i}: ')
            if (line.isspace() or not line): # An empty line ends the command
                target.write('\n')
                break
            target.write(f'{line}\n')
        o.system(f'Closing {path}... ')
    o.done('\n')


def makeDirectory(full_command: str) -> None:
    _, path = p.command(full_command, 2)
    if (not path):
        path = o.argument('Insert missing argument (path): ')
    if (path.isspace() or not path):
        o.abort('No given path')
        return
    path = p.path(path)
    o.system(f'Checking if {path} exists... ')
    try:
        if (d.createIf(path)):
            o.done()
            o.false()
            o.system(f'Created {path}', '\n')
        else:
            o.done()
            o.true()
    except PermissionError:
        print('\n')
        e.PromptPermissionError(f'{path} can\'t be created')
        o.abort(f'Command ended without creating any directory')
        return False


def cleanScreen(full_command: str) -> None:
    _, lines = p.command(full_command, 2)
    print('\n' * int(lines)) if lines else print('\n' * 40)


def moveFolder(full_command: str) -> None:
    _, f, new = p.command(full_command, 3)
    f: str = f if f else o.argument('Insert missing argument (file/folder): ')
    new: str = new if new else o.argument('Insert missing argument (new-path): ')
    if (f.isspace() or not f):
        o.abort('No given file or folder')
        return
    if (new.isspace() or not new):
        o.abort('No given new path')
        return

    f_ = p.path(f)
    new = p.path(new)
    if (os.path.exists(new)):
        new = p.path(new)
    else:
        e.DirectoryException(new)
        o.abort(f'Command ended without moving any directory')
        return

    if (os.path.exists(f_)):
        new_ = p.removeLastFromPath(new)
        o.system(f'Creating {new}... [DONE]') if d.createIf(new_) else None
        o.system(f'Moving everything to {new}... ')
        try:
            sh.move(f_, new)
        except PermissionError:
            e.PromptPermissionError(new)
            o.warn('Some file may miss in the moved directory')
            o.abort('After an error raised, the command has ended')
        o.done('\n')
    else:
        e.DirectoryException(f_)


def loop(full_command: str) -> None:
    _, repetitions, path = p.command(full_command, 3)
    if (not repetitions):
        repetitions = o.argument('Insert value for missing argument (repetitions): ')
    if (not path):
        path = o.argument('Insert value for missing argument (path): ')
    if (repetitions.isspace() or not repetitions):
        o.warn('Invalid value for argument (repetitions)')
        o.system('Value was set to default value: 1')
        repetitions = '1'

    try:
        for i in range(int(repetitions)):
            if (not run(f'run {path}')):
                o.abort(f'Loop aborted after {i+1}th run')
                return
    except RecursionError:
        o.abort(f'Too many recursive calls occurred')


commands = {
    'cd': changePath,
    'close': close,
    'cls': cleanScreen,
    'directory': d.main, # Complex command stored in directory.py
    'echo': echo,
    'end': close,
    'exit': close,
    'help': promptHelp,
    'loop': loop,
    'makedir': makeDirectory,
    'makefile': makeFile,
    'makesource': makeSource,
    'move': moveFolder,
    'path': changePath,
    'quit': close,
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