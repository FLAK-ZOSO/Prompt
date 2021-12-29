#usr/bin/env Python3


def getLine() -> int:
    with open('line.txt', 'r') as line:
        return int(line.read())


def getCurrentPath() -> str:
    with open('current_path.txt', 'r') as c_p:
        return c_p.read()


def incrementLine(increment: int) -> None:
    with open('line.txt', 'r') as line:
        n = int(line.read())
    with open('line.txt', 'w') as line:
        line.write(str(n + increment))