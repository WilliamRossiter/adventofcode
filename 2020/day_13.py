
import math

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
    iBusMax = aryNBus.index(max(aryNBus))
    cArrival = 1
    nTimestampMatching = 0
    while True:
        nTimestampMatching = (aryNBus[iBusMax] * cArrival) - arydMin[iBusMax]
        fIsValid = True
        for iBus in range(len(aryNBus)):
            if (nTimestampMatching + arydMin[iBus]) % aryNBus[iBus] != 0:
                fIsValid = False
                break
        cArrival += 1
        if fIsValid:
            break
    print(nTimestampMatching)

Main('2020/input/day_13.txt')