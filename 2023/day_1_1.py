
import common

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def NFirstInString(str):
    for index, char in enumerate(str):
        if char.isdigit():
            return int(char)
        else:
            for indexDigits, digit in enumerate(digits):
                match = True
                for indexDigit, charDigit in enumerate(digit):
                    if str[index + indexDigit] != charDigit:
                        match = False
                        break
                if match:
                    return indexDigits + 1
    return -1

def NLastInString(str):
    nLast = -1
    for index, char in enumerate(str):
        if char.isdigit():
            nLast = int(char)
        else:
            for indexDigits, digit in enumerate(digits):
                match = True
                for indexDigit, charDigit in enumerate(digit):
                    if (len(str) <= (index + indexDigit)) or str[index + indexDigit] != charDigit:
                        match = False
                        break
                if match:
                    nLast = indexDigits + 1
                    break
    return nLast

def Main():
    aryStrInput = common.AryStrFromFile('2023/input/day_1.txt')
    nSum = 0
    for str in aryStrInput:
        nSum += ((NFirstInString(str) * 10) + NLastInString(str))
    print(nSum)

Main()