
# https://adventofcode.com/2020/day/3

import math
import common
import fileinput

def AryStrRead(strFile):
    aryStr = []
    f = fileinput.input(files=(strFile))
    for strLine in f:
        aryStr.append(strLine.strip())
    f.close()
    return aryStr

def CTreeEncounteredOnSlope(aryStrTreeGrid, cChRow, chTree, dx, dy):
    cTree = 0
    x = 0
    y = 0
    while y < len(aryStrTreeGrid):
        if aryStrTreeGrid[y][x] == chTree:
            cTree += 1
        x = (x + dx) % cChRow
        y = (y + dy)
    return cTree

def NProductOfTreesPerSlope(aryStrTreeGrid, cChRow, chTree, arySlope):
    arycTree = []
    for slope in arySlope:
        arycTree.append(CTreeEncounteredOnSlope(aryStrTreeGrid, cChRow, chTree, slope[0], slope[1]))
    nProduct = 1
    for cTree in arycTree:
        nProduct *= cTree
    return nProduct

def Main():
    aryStr = AryStrRead('2020/input/day_3.txt');
    arySlope = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(NProductOfTreesPerSlope(aryStr, len(aryStr[0]), '#', [(3, 1)]))
    print(NProductOfTreesPerSlope(aryStr, len(aryStr[0]), '#', arySlope))

Main()