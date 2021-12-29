#usr/bin/env Python3
import perform as p


def main():
    # Reset default values
    with open('current_path.txt', 'w+') as current:
        current.write('C:\\')
    with open('line.txt', 'w+') as line:
        line.write('0')

    while (True):
        if (p.main()):
            break # If they use the command "quit"


if (__name__ == '__main__'):
    main()
