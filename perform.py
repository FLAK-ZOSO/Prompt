#!/usr/bin/env Python3
import commands as c
import comments as comm
import exceptions as e
import variables as v


def main(command: str) -> (bool | str):
    current_path = v.getCurrentPath()
    commands = c.commands

    command = comm.checkComments(command)
    if (not command or command.isspace()):
        return False

    try: # Better ask for forgiveness than for permission
        commands[command.split()[0].lower()](command)
        command = command.split()[0].lower()
    except KeyError:
        if (command in ['close', 'end', 'exit', 'quit']):
            c.close(current_path)
            return True # The main.main function ends
        else:
            e.CommandException(command)
            return '' # It's False too, but it says that the CommandException was catched
    
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main('')