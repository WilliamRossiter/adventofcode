
import common
import re

def Main():
    aryStrInput = common.AryStrFromFile('2023/input/day_2.txt')
    nSumPower = 0
    for str in aryStrInput:
        match = re.match(r"Game (\d+): (.*)", str)
        nGame = int(match.group(1))
        rolls = match.group(2).split(";")
        nMinPerColor = [0, 0, 0]
        for roll in rolls:
            dice = roll.split(",")
            for die in dice:
                matchDie = re.match(r" ?(\d+) (.+)", die)
                nRollNumber = int(matchDie.group(1))
                strColor = matchDie.group(2)
                if (strColor == "red"):
                    nMinPerColor[0] = max(nMinPerColor[0], nRollNumber)
                elif (strColor == "green"):
                    nMinPerColor[1] = max(nMinPerColor[1], nRollNumber)
                elif (strColor == "blue"):
                    nMinPerColor[2] = max(nMinPerColor[2], nRollNumber)
        nSumPower += (nMinPerColor[0] * nMinPerColor[1] * nMinPerColor[2])
    print(nSumPower)

Main()