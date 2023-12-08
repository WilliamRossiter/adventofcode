
import common
import re
import math

class ScratchCard:
    def __init__(self, cardInput):
        self.copies = 1
        self.winningNumbers = []
        self.myNumbers = []
        match = re.match(r"Card +\d+: ([ \d]+) \| ([ \d]+)", cardInput)
        for num in match.group(1).split(" "):
            if num.isdigit():
                self.winningNumbers.append(int(num))
        for num in match.group(2).split(" "):
            if num.isdigit():
                self.myNumbers.append(int(num))

    def matchingNumbers(self):
        winningNumbersCur = 0
        for number in self.myNumbers:
            if number in self.winningNumbers:
                winningNumbersCur += 1
        return winningNumbersCur

    def pointValue(self):
        return int(2 ** (self.matchingNumbers() - 1))

def Main():
    aryStrInput = common.AryStrFromFile('2023/input/day_4.txt')
    totalPointValue = 0
    scratchCards = []
    copiesTotal = 0
    for str in aryStrInput:
        scratchCards.append(ScratchCard(str))
    for index, scratchCard in enumerate(scratchCards):
        winningNumbersCur = scratchCard.matchingNumbers()
        copiesCur = scratchCard.copies
        for i in range(winningNumbersCur):
            scratchCards[index + i + 1].copies += copiesCur
        copiesTotal += copiesCur
        totalPointValue += scratchCard.pointValue()
    print("Day 4_1 Answer: {}".format(totalPointValue))
    print("Day 4_2 Answer: {}".format(copiesTotal))

Main()