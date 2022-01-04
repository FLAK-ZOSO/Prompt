#!/usr/bin/env Python3
import perform as pe
import variables as v


def parse(path: str) -> list[str]:
    with open(path, 'r') as commands:
        lines = commands.read().split('\n')
    return lines


def run(path: str) -> None:
    for line in parse(path):
        if ('run' in line or 'loop' in line): # Check for recursive call
            if (path in line or path.removesuffix('.txt') in line):
                print('[ABORT] This source file was calling or looping over itself')
                v.incrementLine(1)
                return
            else:
                print('[WARNING] This source file is calling or looping over an other file')
                v.incrementLine(1)
        if (pe.main(line)):
            return