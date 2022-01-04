#!/usr/bin/env Python3
import json


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
        print('{The variable verbose was not bool-typed. It has been reset to True}')
        return True


def getEcho() -> bool:
    with open('var/echo.json', 'r') as echo:
        return json.load(echo)


def resetEcho() -> None:
    print('Opening echo.json in write mode... ', end='')
    with open('var/echo.json', 'w') as line:
        print('[DONE]')
        json.dump(True, line)
        print('Closing echo.json... ', end='')
    print('[DONE]\n')


def currentPathAsDefault() -> None:
    print('Opening default_path.txt in write mode... ', end='')
    with open('var/default_path.txt', 'w+') as default:
        print('[DONE]')
        print('Opening current_path.txt in read mode... ', end='')
        with open('var/current_path.txt', 'r') as current:
            print('[DONE]')
            print('Closing current_path.txt... ', end='')
            default.write(new := current.read())
        print('[DONE]')
        print('Closing default_path.txt... ', end='')
    print('[DONE]')
    print(f'Now the default path is {new}\n')


def defaultPathAsCurrent() -> None:
    print('Opening current_path.txt in write mode... ', end='')
    with open('var/current_path.txt', 'w+') as current:
        print('[DONE]')
        print('Opening default_path.txt in read mode... ', end='')
        with open('var/default_path.txt', 'r') as default:
            print('[DONE]')
            print('Closing default_path.txt... ', end='')
            current.write(d := default.read())
        print('[DONE]')
        print('Closing current_path.txt... ', end='')
    print('[DONE]')
    print(f'Now the path is {d}\n')


def customPathAsCurrent(new: str) -> None:
    print('Opening current_path.txt in write mode... ', end='')
    with open('var/current_path.txt', 'w') as current:
        print('[DONE]')
        print('Closing current_path.txt... ', end='')
        current.write(new)
    print('[DONE]')