#!usr/bin/env Python3
import output as o


# Global variable to tell if the current line is part of a comment
comment: bool = False


def checkComments(text: str) -> str:
    global comment
    if (comment):
        if ('*\\' in text):
            text = text.split('*\\', 1)[1].removeprefix('*\\')
            comment = False
            if ('/*' in text or '*\\' in text):
                return checkComments(text)
        else:
            return ''
    else: # There was no previous unclosed comment tag
        if ('/*' in text and '*\\' in text):
            uncommented = text.split('/*')[0]
            comment = True
            return uncommented + checkComments(text.split('/*', 1)[1]) # Recursive call
        elif ('/*' in text):
            commented_text: str = text[text.find('/*'):]
            text = text.removesuffix(commented_text)
            comment = True
        elif ('*\\' in text):
            o.warn('Closing comment character (*\\) found in command without opening comment character')
    # Check for inline comments
    if ('//' in text):
        text = text.split('//', 1)[0]
    if (any([chars in text for chars in ['/*', '*\\', '//']])): # Uncaught comments
        return checkComments(text) # Recursive call
    return text