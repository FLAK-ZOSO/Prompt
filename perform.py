#usr/bin/env Python3
import commands as c
import exceptions as e
import variables as v


def main() -> bool:
    current_path = v.getCurrentPath()
    line_ = v.getLine()
    commands = c.commands

    if (v.getEcho()):
        command = input(f'{line_}: {current_path}> ')
    else:
        command = input()
    v.incrementLine(1)

    if (command == '' or command.isspace()):
        return False

    try: # Better ask for forgiveness than for permission
        commands[command.split()[0].lower()](command)
        command = command.split()[0].lower()
    except KeyError:
        if (command in ['quit', 'close', 'end', 'exit']):
            c.close(current_path)
            return True # The main.main function ends
        else:
            e.CommandException(command)
        v.incrementLine(1)
    
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main()