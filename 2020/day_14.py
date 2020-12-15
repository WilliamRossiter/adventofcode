
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

def SetMemFloating(addrPartial, val, mem):
    addrFinal = 0
    for iBit in range(len(addrPartial)):
        bit = addrPartial[iBit]
        if (bit == '1'):
            addrFinal += (1 << iBit)
        elif (bit == 'X'):
            addrPartial0 = addrPartial.copy()
            addrPartial0[iBit] = '0'
            SetMemFloating(addrPartial0, val, mem)
            addrPartial1 = addrPartial.copy()
            addrPartial1[iBit] = '1'
            SetMemFloating(addrPartial1, val, mem)
            return
    mem[addrFinal] = val

def SetMem2(addr, mask, val, mem):
    addrPartial = []
    for iBit in range(len(mask)):
        bit = mask[iBit]
        if (bit == '1'):
            addrPartial.append('1')
        elif (bit == 'X'):
            addrPartial.append('X')
        elif (((1 << iBit) & addr) != 0):
            addrPartial.append('1')
        else:
            addrPartial.append('0')
    SetMemFloating(addrPartial, val, mem)

def RunProgramDecoder2(program, mem):
    mask = []
    for instr in program:
        if (instr[0] == 'mask'):
            mask = instr[1]
        else:
            SetMem2(instr[1], mask, instr[2], mem)

def Main(strFile):
    program = ProgramParse(strFile)
    mem = {}
    RunProgramDecoder1(program, mem)
    print(SumOfDictEntries(mem))
    mem = {}
    RunProgramDecoder2(program, mem)
    print(SumOfDictEntries(mem))

Main('2020/input/day_14.txt')