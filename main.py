#usr/bin/env Python3
import perform as p
import variables as v


def main():
    # Reset default values
    with open('line.txt', 'w+') as line:
        line.write('0')
    v.defaultPathAsCurrent()

    while (True):
        if (p.main()):
            break # If they use the command "quit"


if (__name__ == '__main__'):
    main()
