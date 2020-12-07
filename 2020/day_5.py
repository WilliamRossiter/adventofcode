
# https://adventofcode.com/2020/day/5

def AryStrSeatRead(strFile):
    with open(strFile) as f:
        return f.read().split('\n')

def ArySeatIdFromAryStrSeat(aryStrSeat, cRow, cCol):
    arySeatId = []
    for strSeat in aryStrSeat:
        iRowMic = 0
        iRowMac = cRow
        iColMic = 0
        iColMac = cCol
        for iCh in range(len(strSeat)):
            ch = strSeat[iCh]
            diRow = (iRowMac - iRowMic) / 2
            diCol = (iColMac - iColMic) / 2
            if ch == 'F':
                iRowMac -= diRow
            elif ch == 'B':
                iRowMic += diRow
            elif ch == 'L':
                iColMac -= diCol
            elif ch == 'R':
                iColMic += diCol
        arySeatId.append(iRowMic * 8 + iColMic)
    return arySeatId

def ArySeatIdMissingInRange(seatIdMic, seatIdMac, arySeatId):
    arySeatIdAll = range(seatIdMic, seatIdMac)
    for seatId in arySeatId:
        arySeatIdAll.remove(seatId)
    return arySeatIdAll

def Main():
    cRow = 128
    cCol = 8
    aryStrSeat = AryStrSeatRead('2020/input/day_5.txt');
    arySeatId = ArySeatIdFromAryStrSeat(aryStrSeat, cRow, cCol)
    arySeatIdMissing = ArySeatIdMissingInRange(0, cRow * 8 + cCol, arySeatId)
    print(max(arySeatId))
    print(arySeatIdMissing)

Main()