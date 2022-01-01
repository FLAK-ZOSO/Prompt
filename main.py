#usr/bin/env Python3
import perform as p
import variables as v


def main():
    # Reset default values
    v.resetLine()
    v.resetEcho()
    v.defaultPathAsCurrent()

    while (True):
        if (v.getEcho()):
            command = input(f'{v.getLine()}: {v.getCurrentPath()}> ')
        else:
            command = input()
        v.incrementLine(1)
        if (p.main(command)):
            break # If they use the command "quit"


if (__name__ == '__main__'):
    main()