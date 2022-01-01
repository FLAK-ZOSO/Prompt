#usr/bin/env Python3
import parsing as p
import perform as pe
import os
import variables as v


def parse(path: str) -> list[str]:
    with open(path, 'r') as commands:
        lines = commands.read().split('\n')
    return lines


def run(path: str) -> None:
    for line in parse(path):
        if (pe.main(line)):
            return