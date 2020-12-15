
import re

def SumOfDictEntries(mem):
    sum = 0
    for v in mem.values():
        sum += v
    return sum

def ApplyMask(val, mask):
    for iBit in range(len(mask)):
        bit = mask[iBit]
        if (bit == 0):
            val &= ~(1 << iBit)
        elif (bit == 1):
            val |= (1 << iBit)
    return val

def ProgramParse(strFile):
    program = []
    with open(strFile) as f:
        for line in f:
            aryStrPart = line.split(' = ')
            val = aryStrPart[1].strip()
            if aryStrPart[0] == 'mask':
                instr = 'mask'
                mask = list(val)
                mask.reverse()
                program.append((instr, mask))
            else:
                instr = 'mem'
                reMatch = re.match('\w+\[(\d+)\]', aryStrPart[0])
                addr = int(reMatch[1])
                program.append((instr, addr, int(val)))
    return program

def RunProgramDecoder1(program, mem):
    mask = []
    for instr in program:
        if (instr[0] == 'mask'):
            mask = []
            for iCh in range(len(instr[1])):
                ch = instr[1][iCh]
                if (ch == '0'):
                    mask.append(0)
                elif (ch == '1'):
                    mask.append(1)
                else:
                    mask.append(-1)
        else:
            mem[instr[1]] = ApplyMask(instr[2], mask)

def AddMaskCombinations(maskBase, masks):
    for iBit in range(len(maskBase)):
        bit = maskBase[iBit]
        if (bit == -1):
            maskBase0 = maskBase.copy()
            maskBase0[iBit] = 0
            AddMaskCombinations(maskBase0, masks)
            maskBase1 = maskBase.copy()
            maskBase1[iBit] = 1
            AddMaskCombinations(maskBase1, masks)
            return
    masks.append(maskBase)

def RunProgramDecoder2(program, mem):
    maskBase = []
    masks = []
    for instr in program:
        if (instr[0] == 'mask'):
            maskBase = []
            masks = []
            for iCh in range(len(instr[1])):
                ch = instr[1][iCh]
                if (ch == '0'):
                    maskBase.append(0)
                elif (ch == '1'):
                    maskBase.append(1)
                else:
                    maskBase.append(-1)
            AddMaskCombinations(maskBase, masks)
        else:
            for mask in masks:
                addr = ApplyMask(instr[1], mask)
                mem[addr] = instr[2]

def Main(strFile):
    program = ProgramParse(strFile)
    mem = {}
    #RunProgramDecoder1(program, mem)
    RunProgramDecoder2(program, mem)
    print(mem)
    print(SumOfDictEntries(mem))

Main('2020/input/day_14.txt')