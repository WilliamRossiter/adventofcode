
# https://adventofcode.com/2020/day/9



def FIsValidNumber(n, aryNPreamble):
    for i in range(len(aryNPreamble)):
        for j in range(i, len(aryNPreamble)):
            if ((aryNPreamble[i] + aryNPreamble[j]) == n):
                return True
    return False

def NSumFromArray(aryN):
    nSum = 0
    for n in aryN:
        nSum += n
    return nSum

def AryNWithSum(aryN, nSum):
    aryNSum = []
    for n in aryN:
        aryNSum.append(n)
        nSumCur = NSumFromArray(aryNSum)
        while nSumCur > nSum:
            aryNSum.pop(0)
            nSumCur = NSumFromArray(aryNSum)
        if nSumCur == nSum:
            return aryNSum

def NInvalidNumber(aryN, cPreamble):
    iRow = 0
    aryNPreamble = []
    for n in aryN:
        if iRow < cPreamble:
            aryNPreamble.append(n)
        elif FIsValidNumber(n, aryNPreamble):
            aryNPreamble.pop(0)
            aryNPreamble.append(n)
        else:
            return n
        iRow += 1

def Main(strFile):
    with open(strFile) as f:
        aryStrN = f.read().split('\n')
        aryN = []
        for strN in aryStrN:
            aryN.append(int(strN))
        nInvalidNumber = NInvalidNumber(aryN, 25)
        print(nInvalidNumber)
        aryNWithSum = AryNWithSum(aryN, nInvalidNumber)
        print(max(aryNWithSum) + min(aryNWithSum))

Main('2020/input/day_9.txt')