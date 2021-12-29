#usr/bin/env Python3
import directory as d
import exceptions as e
import variables as v


def promptHelp() -> None:
    with open('help.txt', 'r') as file:
        print(content := file.read())
    content = content.count('\n')
    v.incrementLine(content)


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
        if (command.lower() in ['quit', 'close', 'end']):
            return True # The main.main function ends
    
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main()