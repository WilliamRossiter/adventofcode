
# https://adventofcode.com/2020/day/10

def NSumFromArray(aryN):
    nSum = 0
    for n in aryN:
        nSum += n
    return nSum

def NProductFromArray(aryN):
    nProduct = 1
    for n in aryN:
        nProduct *= n
    return nProduct

def Main(strFile):
    fibSeq = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    arydN = []
    nUnique = 1
    with open(strFile) as f:
        aryN = [int(n) for n in f.read().split()]
        aryN.sort()
        nPrev = 0
        for n in aryN:
            dn = n - nPrev
            arydN.append(dn)
            nPrev = n
        arydN.append(3)
    aryN1Chain = [0]
    for n in arydN:
        if (n == 1):
            aryN1Chain[-1] += 1
        else:
            aryN1Chain.append(0)
    aryCombo = []
    for n1Chain in aryN1Chain:
        if (n1Chain > 0):
            aryCombo.append(NSumFromArray(fibSeq[0:n1Chain]))
    print(NProductFromArray(aryCombo))
    

Main('2020/input/day_10.txt')