
# https://adventofcode.com/2020/day/7

import re

class BagSpec:
    def __init__(self, strBagSpec):
        aryStrBagSpecSplit = strBagSpec.split(" bags contain ")
        self.m_strBag = aryStrBagSpecSplit[0]
        strBagContains = aryStrBagSpecSplit[1]
        aryStrBagContains = strBagContains.split(', ')
        self.m_aryTupleBagContains = []
        for strBagContains in aryStrBagContains:
            if 'no other bags' not in strBagContains:
                reMatch = re.match('(\d) (\w+ \w+)', strBagContains)
                self.m_aryTupleBagContains.append((int(reMatch.group(1)), reMatch.group(2)))

def AryBagSpecRead(strFile):
    aryBagSpec = []
    with open(strFile) as f:
        aryStrBagSpec = f.read().split("\n")
        for strBagSpec in aryStrBagSpec:
            aryBagSpec.append(BagSpec(strBagSpec))
    return aryBagSpec

def GetBagSpecsThatCanContainBagColor(aryBagSpec, strColor, aryBagSpecCanContain):
    for bagSpec in aryBagSpec:
        for tupleBag in bagSpec.m_aryTupleBagContains:
            if strColor in tupleBag[1]:
                if bagSpec not in aryBagSpecCanContain:
                    aryBagSpecCanContain.append(bagSpec)
                    GetBagSpecsThatCanContainBagColor(aryBagSpec, bagSpec.m_strBag, aryBagSpecCanContain)

def NGetBagsInColor(aryBagSpec, strColor):
    nBag = 0
    for bagSpec in aryBagSpec:
        if strColor in bagSpec.m_strBag:
            for tupleBag in bagSpec.m_aryTupleBagContains:
                nBag += tupleBag[0] + (tupleBag[0] * NGetBagsInColor(aryBagSpec, tupleBag[1]))
    return nBag

def Main():
    aryBagSpec = AryBagSpecRead('2020/input/day_7.txt')
    aryBagSpecCanContain = []
    GetBagSpecsThatCanContainBagColor(aryBagSpec, 'shiny gold', aryBagSpecCanContain)
    print(len(aryBagSpecCanContain))
    print(NGetBagsInColor(aryBagSpec, 'shiny gold'))

Main()