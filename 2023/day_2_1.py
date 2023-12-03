
import common
import re

def Main():
    aryStrInput = common.AryStrFromFile('2023/input/day_2.txt')
    nPossibleGames = 0
    for str in aryStrInput:
        match = re.match(r"Game (\d+): (.*)", str)
        nGame = int(match.group(1))
        rolls = match.group(2).split(";")
        impossible = False
        for roll in rolls:
            dice = roll.split(",")
            for die in dice:
                matchDie = re.match(" ?(\d+) (.+)", die)
                nRollNumber = int(matchDie.group(1))
                strColor = matchDie.group(2)
                if (strColor == "red" and nRollNumber > 12):
                    impossible = True
                    break
                elif (strColor == "green" and nRollNumber > 13):
                    impossible = True
                    break
                elif (strColor == "blue" and nRollNumber > 14):
                    impossible = True
                    break
            if impossible:
                break
        if not impossible:
            nPossibleGames += nGame
    print(nPossibleGames)

Main()