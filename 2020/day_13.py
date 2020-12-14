
import math

def NProductFromArray(aryN):
    nProduct = 1
    for n in aryN:
        nProduct *= n
    return nProduct

def Main(strFile):
    aryStrInput = []
    with open(strFile) as f:
        aryStrInput = f.read().split()
    nMinLeaving = int(aryStrInput[0])
    aryNBus = []
    arydMin = []
    dMin = 0
    aryStrBus = aryStrInput[1].split(',')
    for strBus in aryStrBus:
        if (strBus != 'x'):
            aryNBus.append(int(strBus))
            arydMin.append(dMin)
        dMin += 1
    nMinWaitLeast = max(aryNBus)
    nBusLeast = None
    for nBus in aryNBus:
        if nBus == 0:
            continue
        div = math.ceil(nMinLeaving / nBus)
        nMinArrive = div * nBus
        nMinWait = nMinArrive - nMinLeaving
        if (nMinWait < nMinWaitLeast):
            nBusLeast = nBus
            nMinWaitLeast = nMinWait
    print (nMinWaitLeast * nBusLeast)
    nTimestamp = aryNBus[0]
    nIncr = aryNBus[0]
    cBus = 1
    while cBus <= len(aryNBus):
        while True:
            fIsValid = True
            for iBus in range(len(aryNBus[:cBus])):
                if (nTimestamp + arydMin[iBus]) % aryNBus[iBus] != 0:
                    fIsValid = False
                    break
            if fIsValid:
                break
            else:
                nTimestamp += nIncr
        nIncr = NProductFromArray(aryNBus[:cBus])
        cBus += 1
    print(nTimestamp)

Main('2020/input/day_13.txt')