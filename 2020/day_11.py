
import copy

def ChSeat(aryRowSeat, iRow, iCol):
    if (iRow < 0 or iRow >= len(aryRowSeat) or iCol < 0 or iCol >= len(aryRowSeat[0])):
        return None 
    return aryRowSeat[iRow][iCol]  

def Main(strFile):
    aryStrRow = []
    with open(strFile) as f:
        for line in f:
            aryStrRow.append(list(line.strip('\n')))
    cCol = len(aryStrRow[0])
    aryStrRowPrev = copy.deepcopy(aryStrRow)
    aryStrRowNext = copy.deepcopy(aryStrRow)
    aryNearbySeat = [[-1, -1,], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    while True:
        for iRow in range(len(aryStrRow)):
            for iCol in range(cCol):
                chSeat = aryStrRowPrev[iRow][iCol]
                if chSeat == 'L':
                    fHasOccupiedSeat = False
                    for nearbySeat in aryNearbySeat:
                        iRowNearby = iRow + nearbySeat[0]
                        iColNearby = iCol + nearbySeat[1]
                        chNearbySeat = ChSeat(aryStrRowPrev, iRowNearby, iColNearby)
                        while chNearbySeat == '.':
                            iRowNearby = iRowNearby + nearbySeat[0]
                            iColNearby = iColNearby + nearbySeat[1]
                            chNearbySeat = ChSeat(aryStrRowPrev, iRowNearby, iColNearby)
                        if (chNearbySeat == '#'):
                            fHasOccupiedSeat = True
                            break
                    if not fHasOccupiedSeat:
                        aryStrRowNext[iRow][iCol] = '#'
                elif chSeat == '#':
                    cOccupiedSeat = 0
                    for nearbySeat in aryNearbySeat:
                        iRowNearby = iRow + nearbySeat[0]
                        iColNearby = iCol + nearbySeat[1]
                        chNearbySeat = ChSeat(aryStrRowPrev, iRowNearby, iColNearby)
                        while chNearbySeat == '.':
                            iRowNearby = iRowNearby + nearbySeat[0]
                            iColNearby = iColNearby + nearbySeat[1]
                            chNearbySeat = ChSeat(aryStrRowPrev, iRowNearby, iColNearby)
                        if (chNearbySeat == '#'):
                            cOccupiedSeat += 1
                            continue
                    if cOccupiedSeat >= 5:
                        aryStrRowNext[iRow][iCol] = 'L'

        if (aryStrRowPrev == aryStrRowNext):
            break
        else:
            aryStrRowPrev = copy.deepcopy(aryStrRowNext)
    cOccupied = 0
    for aryRow in aryStrRowNext:
        for chCol in aryRow:
            if chCol == '#':
                cOccupied += 1
    print(cOccupied)

Main('2020/input/day_11.txt')