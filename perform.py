#!/usr/bin/env Python3
import commands as c
import exceptions as e
import re
import variables as v

# Global variable to tell if the current line is part of a comment
comment: bool = False


def checkComments(text: str) -> str:
    global comment
    if (comment):
        if ('*\\' in text):
            text = text.split('*\\')[1].removeprefix('*\\')
            comment = False
            if ('/*' in text or '*\\' in text):
                return checkComments(text)
        else:
            return ''
    else: # There was no previous unclosed comment tag
        if ('/*' in text and '*\\' in text):
            uncommented = text.split('/*')[0]
            comment = True
            return uncommented + checkComments(text.split('/*')[1]) # Recursive call
        elif ('/*' in text):
            commented_text: str = text[text.find('/*'):]
            text = text.removesuffix(commented_text)
            comment = True
        elif ('*\\' in text):
            e.o.warn('Closing comment character (*\\) found in command without opening comment character')
    # Check for inline comments
    if ('//' in text):
        text = text.split('//', 1)[0]
    if (any([chars in text for chars in ['/*', '*\\', '//']])): # Uncaught comments
        return checkComments(text) # Recursive call
    return text


def main(command: str) -> bool:
    current_path = v.getCurrentPath()
    commands = c.commands

    command = checkComments(command)
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
    
    return False # The main.main function re-calls perform.main


if (__name__ == '__main__'):
    main('')