
import common
import re
import math

class ScratchCard:
    def __init__(self, cardInput):
        self.winningNumbers = []
        self.myNumbers = []
        match = re.match(r"Card +\d+: ([ \d]+) \| ([ \d]+)", cardInput)
        for num in match.group(1).split(" "):
            if num.isdigit():
                self.winningNumbers.append(int(num))
        for num in match.group(2).split(" "):
            if num.isdigit():
                self.myNumbers.append(int(num))

    def pointValue(self):
        winningNumbers = 0
        for number in self.myNumbers:
            if number in self.winningNumbers:
                winningNumbers += 1
        return int(2 ** (winningNumbers - 1))

def Main():
    aryStrInput = common.AryStrFromFile('2023/input/day_4.txt')
    totalPointValue = 0
    for str in aryStrInput:
        scratchCard = ScratchCard(str)
        print(scratchCard.pointValue())
        totalPointValue += scratchCard.pointValue()
    print(totalPointValue)

Main()