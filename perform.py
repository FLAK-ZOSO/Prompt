#!/usr/bin/env Python3
import commands as c
import comments as comm
import exceptions as e


def main(command: str) -> (bool | str):
    command = comm.checkComments(command)
    if (command.isspace() or not command):
        return False

    try: # Better ask for forgiveness than for permission
        c.commands[cmd := command.split()[0].lower()](command)
    except KeyError:
        e.CommandException(cmd)
        return '' # It's False too, but it says that the CommandException was catched
    
    if (cmd in ['close', 'end', 'exit', 'quit']):
        return True # The main.main function ends
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main('')