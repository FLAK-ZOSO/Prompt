#usr/bin/env Python3


def getLine() -> int:
    with open('line.txt', 'r') as line:
        return int(line.read())


def getCurrentPath() -> str:
    with open('current_path.txt', 'r') as c_p:
        return c_p.read()


def getDefaultPath() -> str:
    with open('default_path.txt', 'r') as d_p:
        return d_p.read()


def incrementLine(increment: int) -> None:
    with open('line.txt', 'r') as line:
        n = int(line.read())
    with open('line.txt', 'w') as line:
        line.write(str(n + increment))


def resetLine() -> None:
    print('Opening line.txt in write mode... ', end='')
    with open('line.txt', 'w') as line:
        print('[DONE]')
        line.write('0'),
        print('Closing line.txt... ', end='')
    print('[DONE]\n')
    incrementLine(3)


def currentPathAsDefault() -> None:
    print('Opening default_path.txt in write mode... ', end='')
    with open('default_path.txt', 'w+') as default:
        print('[DONE]')
        print('Opening current_path.txt in read mode... ', end='')
        with open('current_path.txt', 'r') as current:
            print('[DONE]')
            print('Closing current_path.txt... ', end='')
            default.write(new := current.read())
        print('[DONE]')
        print('Closing default_path.txt... ', end='')
    print('[DONE]')
    print(f'Now the default path is {new}\n')
    incrementLine(6)


def defaultPathAsCurrent() -> None:
    print('Opening current_path.txt in write mode... ', end='')
    with open('current_path.txt', 'w+') as current:
        print('[DONE]')
        print('Opening default_path.txt in read mode... ', end='')
        with open('default_path.txt', 'r') as default:
            print('[DONE]')
            print('Closing default_path.txt... ', end='')
            current.write(d := default.read())
        print('[DONE]')
        print('Closing current_path.txt... ', end='')
    print('[DONE]')
    print(f'Now the path is {d}\n')
    incrementLine(6)