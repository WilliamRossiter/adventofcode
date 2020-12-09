
# https://adventofcode.com/2020/day/8

import re
import copy

def FTryRunProgram(aryInstr):
    iInstr = 0
    nAcc = 0
    while iInstr < len(aryInstr):
        instr = aryInstr[iInstr]
        if instr[2] == 1:
            print('infinite loop! nAcc is %d' % nAcc)
            return False
        instr[2] = 1
        if instr[0] == 'acc':
            nAcc += instr[1]
            iInstr += 1
        elif instr[0] == 'jmp':
            iInstr += instr[1]
        else:
            iInstr += 1
    print(nAcc)
    return True

def FlipInstruction(aryInstr, cFlippedInstr):
    for instr in aryInstr:
        if instr[0] == 'jmp' or instr[0] == 'nop':
            cFlippedInstr -= 1
            if cFlippedInstr == 0:
                if instr[0] == 'jmp':
                    instr[0] = 'nop'
                else:
                    instr[0] = 'jmp'
                return

def Main(strFile):
    with open(strFile) as f:
        aryStrInstr = f.read().split('\n')
        aryInstr = []
        for strInstr in aryStrInstr:
            reMatch = re.match('(\w+) ([\+-]\d+)', strInstr)
            aryInstr.append([reMatch.group(1), int(reMatch.group(2)), 0])
        cFlippedInstr = 0
        aryInstrCur = copy.deepcopy(aryInstr)
        while not FTryRunProgram(aryInstrCur):
            cFlippedInstr += 1
            aryInstrCur = copy.deepcopy(aryInstr)
            FlipInstruction(aryInstrCur, cFlippedInstr)

Main('2020/input/day_8.txt')