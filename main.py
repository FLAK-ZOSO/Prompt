#usr/bin/env Python3
import directory as d


__author__ = 'FLAK-ZOSO'
__version__ = 'v0.0.1'


if __name__ == '__main__':

    base_path = input('Base path: ')
    name = input('Name of the folder: ')
    dept = int(input('How many subdirectories will your folder be in? '))
    sub = int(input('How many subdirectories will your folder contain? '))
    print('\n\n')
    
    sup = d.getSupList(dept)
    sub = d.getSubList(sub)
    path, worked = d.createFull(base_path, name, sup, sub)
    d.open(path)