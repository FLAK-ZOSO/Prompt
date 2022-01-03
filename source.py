#!/usr/bin/env Python3
import perform as pe
import variables as v


def parse(path: str) -> list[str]:
    with open(path, 'r') as commands:
        lines = commands.read().split('\n')
    return lines


def run(path: str) -> None:
    for line in parse(path):
        if ('run' in line): # Check for recursive call
            if (path in line or path.removesuffix('.txt')):
                print('[ABORT] This source file was calling itself')
                v.incrementLine(1)
                return
            else:
                print('[WARNING] This source file is using a dangerous command: run')
                v.incrementLine(1)
        if (pe.main(line)):
            return