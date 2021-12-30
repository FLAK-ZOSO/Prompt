#usr/bin/env Python3
import perform as p
import variables as v


def main():
    # Reset default values
    v.resetLine()
    v.defaultPathAsCurrent()

    while (True):
        if (p.main()):
            break # If they use the command "quit"


if (__name__ == '__main__'):
    main()