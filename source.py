#!/usr/bin/env Python3
import output as o
import perform as pe


def parse(path: str) -> list[str]:
    with open(path, 'r') as commands:
        lines = commands.read().split('\n')
    return lines


def run(path: str) -> None:
    for line in parse(path):
        if ('run' in line or 'loop' in line): # Check for recursive call
            if (path in line or path.removesuffix('.txt') in line):
                o.abort('This source file was calling or looping over itself')
                return
            else:
                o.warn('This source file is calling or looping over an other file')
        if (pe.main(line)):
            return