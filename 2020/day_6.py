
# https://adventofcode.com/2020/day/6

def NUniqueYesAnswers(strGroup):
    aryStrMember = strGroup.split()
    dictAnswer = {}
    for strMember in aryStrMember:
        for ch in strMember:
            dictAnswer[ch] = 1
    return len(dictAnswer.keys())

def NSumUniqueAnswers(aryStrGroup):
    nSum = 0
    for strGroup in aryStrGroup:
        nSum += NUniqueYesAnswers(strGroup)
    return nSum

def NSharedYesAnswers(strGroup):
    aryStrMember = strGroup.split()
    dictAnswer = {}
    for strMember in aryStrMember:
        for ch in strMember:
            if ch in dictAnswer:
                dictAnswer[ch] += 1
            else:
                dictAnswer[ch] = 1
    nShared = 0
    for key in dictAnswer.keys():
        if dictAnswer[key] == len(aryStrMember):
            nShared += 1
    return nShared

def NSumSharedAnswers(aryStrGroup):
    nSum = 0
    for strGroup in aryStrGroup:
        nSum += NSharedYesAnswers(strGroup)
    return nSum

def AryStrGroupRead(strFile):
    with open(strFile) as f:
        return f.read().split("\n\n")

def Main():
    aryStrGroup = AryStrGroupRead('2020/input/day_6.txt')
    print(NSumUniqueAnswers(aryStrGroup))
    print(NSumSharedAnswers(aryStrGroup))

Main()