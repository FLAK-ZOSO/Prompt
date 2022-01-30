#!/usr/bin/env Python3
import output as o
import perform as p
import variables as v

__author__ = 'FLAK-ZOSO'
__documentation__ = 'https://flak-zoso.github.io/src/repo/Prompt/about.html'
__version__ = 'v1.2.0-beta'
__code__ = f'https://github.com/FLAK-ZOSO/Prompt/tree/{__version__}'


def start() -> None:
    # Reset default values
    v.resetEcho()
    v.defaultPathAsCurrent()
    o.documentation(f'Documentation at {__documentation__} ')
    o.documentation(f'Source code at {__code__} ')
    o.documentation(f'Prompt.py {__version__} by {__author__} is running...', '\n\n')


def main() -> None:
    start()
    while (True):
        line = f'{o.Back.MAGENTA}{o.Fore.WHITE}{v.getCurrentPath()}>{o.Style.RESET_ALL}'
        command = input(line) if v.getEcho() else input()
        if (p.main(command)):
            break # If they use the command "quit"


if (__name__ == '__main__'):
    main()