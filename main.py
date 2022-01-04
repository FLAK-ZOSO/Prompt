#!/usr/bin/env Python3
import perform as p
import variables as v

__author__ = 'FLAK-ZOSO'
__documentation__ = 'https://flak-zoso.github.io/src/repo/Prompt/about.html'
__version__ = 'v0.10.0'
__code__ = 'https://github.com/FLAK-ZOSO/Prompt/tree/' + __version__


def start() -> None:
    # Reset default values
    v.resetLine()
    v.resetEcho()
    v.defaultPathAsCurrent()
    print(f'Documentation at {__documentation__}')
    print(f'Source code at {__code__}')
    print(f'Prompt.py {__version__} by {__author__} is running...\n')
    v.incrementLine(4)


def main() -> None:
    start()
    while (True):
        line = f'{v.getLine()}: {v.getCurrentPath()}> '
        command = input(line) if v.getEcho() else input()
        v.incrementLine(1)
        if (p.main(command)):
            break # If they use the command "quit"


if (__name__ == '__main__'):
    main()