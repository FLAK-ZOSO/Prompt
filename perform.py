#usr/bin/env Python3
import directory as d
import exceptions as e
import parsing as p
import variables as v


def promptHelp() -> None:
    with open('help.txt', 'r') as file:
        print(content := file.read())
    content = content.count('\n')
    v.incrementLine(content)


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
    'help': promptHelp
}


def main() -> bool:
    with open('current_path.txt', 'r') as current:
        current_path = current.read()
    with open('line.txt', 'r') as line:
        line_ = line.read()
    global commands

    command = input(f'{line_}: {current_path}>')

    try: # Better ask for forgiveness than for permission
        commands[command]()
    except KeyError:
        if (command.lower() in ['quit', 'close', 'end', 'exit']):
            close(current_path)
            return True # The main.main function ends
        elif (command == ''):
            pass
        else:
            e.CommandException(command)
        v.incrementLine(1)
    
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main()