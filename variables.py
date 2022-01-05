#!/usr/bin/env Python3
import json
import output as o


types = {
    'bool': bool,
    'float': float,
    'int': int,
    'str': str,
}


def getCurrentPath() -> str:
    with open('var/current_path.txt', 'r') as c_p:
        return c_p.read()


def getDefaultPath() -> str:
    with open('var/default_path.txt', 'r') as d_p:
        return d_p.read()


def getVerbose() -> bool:
    with open('var/verbose.json', 'r') as verbose:
        verbose = verbose.read()
        if (isinstance(json.loads(verbose), bool)):
            return json.loads(verbose)
    with open('var/verbose.json', 'w') as verbose:
        json.dump(True, verbose)
        o.warn('The variable verbose was not bool-typed. It has been reset to True')
        return True


def getEcho() -> bool:
    with open('var/echo.json', 'r') as echo:
        return json.load(echo)


def resetEcho() -> None:
    o.system('Opening echo.json in write mode... ')
    with open('var/echo.json', 'w') as line:
        o.done('\n')
        json.dump(True, line)
        o.system('Closing echo.json... ')
    o.done()
    print('\n\n')


def currentPathAsDefault() -> None:
    o.system('Opening default_path.txt in write mode... ')
    with open('var/default_path.txt', 'w+') as default:
        o.done('\n')
        o.system('Opening current_path.txt in read mode... ')
        with open('var/current_path.txt', 'r') as current:
            o.done('\n')
            o.system('Closing current_path.txt... ')
            default.write(new := current.read())
        o.done('\n')
        o.system('Closing default_path.txt... ')
    o.done('\n')
    o.system(f'Now the default path is {new}\n')


def defaultPathAsCurrent() -> None:
    o.system('Opening current_path.txt in write mode... ')
    with open('var/current_path.txt', 'w+') as current:
        o.done('\n')
        o.system('Opening default_path.txt in read mode... ')
        with open('var/default_path.txt', 'r') as default:
            o.done('\n')
            o.system('Closing default_path.txt... ')
            current.write(d := default.read())
        o.done('\n')
        o.system('Closing current_path.txt... ')
    o.done('\n')
    o.system(f'Now the path is {d}\n')


def customPathAsCurrent(new: str) -> None:
    o.system('Opening current_path.txt in write mode... ')
    with open('var/current_path.txt', 'w') as current:
        o.done('\n')
        o.system('Closing current_path.txt... ')
        current.write(new)
    o.done('\n')