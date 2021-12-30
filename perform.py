#usr/bin/env Python3
import directory as d
import exceptions as e
import parsing as p
import variables as v


def promptHelp(full_command: str=None) -> None:
    with open('help.txt', 'r') as file:
        print(content := file.read())
    content = content.count('\n')
    v.incrementLine(content)


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


global commands
commands = {
    'directory': d.main,
    'help': promptHelp,
    'path': changePath
}


def main() -> bool:
    current_path = v.getCurrentPath()
    line_ = v.getLine()
    global commands

    command = input(f'{line_}: {current_path}> ')

    if (command == ''):
        return False

    try: # Better ask for forgiveness than for permission
        commands[command.split()[0].lower()](command)
        command = command.split()[0].lower()
    except KeyError:
        if (command in ['quit', 'close', 'end', 'exit']):
            close(current_path)
            return True # The main.main function ends
        else:
            e.CommandException(command)
        v.incrementLine(1)
    
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main()