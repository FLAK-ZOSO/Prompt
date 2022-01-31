#!/usr/bin/env Python3
import output as o
import perform as pe


def parse(path: str) -> list[str]:
    with open(path, 'r') as commands:
        lines = commands.read().split('\n')
    return lines


def run(path: str) -> bool:
    for line in parse(path):
        if (line.strip().startswith('run') or line.strip().startswith('loop')): # Check for recursive call
            if (path in line or path.removesuffix('.txt') in line):
                o.abort('This source file was calling or looping over itself')
                return False
            else:
                o.warn('This source file is calling or looping over an other file')
                return False
        if (pe.main(line) == ''):
            return False
    return True