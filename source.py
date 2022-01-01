#usr/bin/env Python3
import os
import variables as v


def parse(path: str) -> list[str]:
    with open(path, 'r') as commands:
        lines = commands.read().split('\n')
    return lines


def run(path: str) -> None:
    commands = 'cd D:\\Python\Python\Prompt | main.py'
    for line in parse(path):
        commands += f' | {line}'
    os.system(commands) # Doesn't work
    v.incrementLine(1)