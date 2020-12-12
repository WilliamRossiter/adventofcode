

def MainSolution1(strFile):
    aryDirection = []
    posCur = (0, 0)
    directionCur = (1, 0)
    with open(strFile) as f:
        aryDirection = f.read().split()
    for direction in aryDirection:
        chDirection = direction[0]
        cDirection = int(direction[1:])
        if (chDirection == 'N'):
            posCur = (posCur[0], posCur[1] + cDirection)
        elif (chDirection == 'S'):
            posCur = (posCur[0], posCur[1] - cDirection)
        elif (chDirection == 'E'):
            posCur = (posCur[0] + cDirection, posCur[1])
        elif (chDirection == 'W'):
            posCur = (posCur[0] - cDirection, posCur[1])
        elif (chDirection == 'L'):
            cTurn = int(cDirection / 90)
            for iTurn in range(cTurn):
                if (directionCur == (1, 0)):
                    directionCur = (0, 1)
                elif (directionCur == (0, 1)):
                    directionCur = (-1, 0)
                elif (directionCur == (-1, 0)):
                    directionCur = (0, -1)
                else:
                    directionCur = (1, 0)
        elif (chDirection == 'R'):
            cTurn = int(cDirection / 90)
            for iTurn in range(cTurn):
                if (directionCur == (1, 0)):
                    directionCur = (0, -1)
                elif (directionCur == (0, -1)):
                    directionCur = (-1, 0)
                elif (directionCur == (-1, 0)):
                    directionCur = (0, 1)
                else:
                    directionCur = (1, 0)
        elif (chDirection == 'F'):
            posCur = (posCur[0] + (directionCur[0] * cDirection), posCur[1] + (directionCur[1] * cDirection))
    print(abs(posCur[0]))
    print(abs(posCur[1]))
    print(abs(posCur[0]) + abs(posCur[1]))

def MainSolution2(strFile):
    aryDirection = []
    posCur = (0, 0)
    waypointCur = (10, 1)
    with open(strFile) as f:
        aryDirection = f.read().split()
    for direction in aryDirection:
        chDirection = direction[0]
        cDirection = int(direction[1:])
        if (chDirection == 'N'):
            waypointCur = (waypointCur[0], waypointCur[1] + cDirection)
        elif (chDirection == 'S'):
            waypointCur = (waypointCur[0], waypointCur[1] - cDirection)
        elif (chDirection == 'E'):
            waypointCur = (waypointCur[0] + cDirection, waypointCur[1])
        elif (chDirection == 'W'):
            waypointCur = (waypointCur[0] - cDirection, waypointCur[1])
        elif (chDirection == 'L'):
            cTurn = int(cDirection / 90)
            for iTurn in range(cTurn):
                waypointCur = (-waypointCur[1], waypointCur[0])
        elif (chDirection == 'R'):
            cTurn = int(cDirection / 90)
            for iTurn in range(cTurn):
                waypointCur = (waypointCur[1], -waypointCur[0])
        elif (chDirection == 'F'):
            posCur = (posCur[0] + (waypointCur[0] * cDirection), posCur[1] + (waypointCur[1] * cDirection))
    print(abs(posCur[0]))
    print(abs(posCur[1]))
    print(abs(posCur[0]) + abs(posCur[1]))

MainSolution2('2020/input/day_12.txt')