
# https://adventofcode.com/2020/day/2

import math
import common
import fileinput


# A password includes a definition of the rules that make that password valid,
#  namely a letter and the range of times that defines the rules of how many
#  instances of it can appear

class Password:
    cLeast = 0
    cMost = 0
    chLetter = ''
    strPassword = ''

    def __init__(self, str):
        aryStrPassword = str.split()
        strRange = aryStrPassword[0]
        aryStrRange = strRange.split('-')
        self.cFirst = int(aryStrRange[0])
        self.cLast = int(aryStrRange[1])
        self.chLetter = aryStrPassword[1][0]
        self.strPassword = aryStrPassword[2]

    def FIsValidOld(self):
        cChRequired = 0
        for i in range(len(self.strPassword)):
            if self.strPassword[i] == self.chLetter:
                cChRequired += 1
        return cChRequired >= self.cFirst and cChRequired <= self.cLast

    def FIsValidNew(self):
        fMatchesFirst = self.strPassword[self.cFirst - 1] == self.chLetter
        fMatchesLast = self.strPassword[self.cLast - 1] == self.chLetter
        return fMatchesFirst != fMatchesLast

def AryPasswordRead(strFile):
    aryPassword = []
    f = fileinput.input(files=(strFile))
    for line in f:
        aryPassword.append(Password(line))
    f.close()
    return aryPassword

def CValidPasswordsOld(aryPassword):
    cPasswordValid = 0
    for password in aryPassword:
        if password.FIsValidOld():
            cPasswordValid += 1
    return cPasswordValid

def CValidPasswordsNew(aryPassword):
    cPasswordValid = 0
    for password in aryPassword:
        if password.FIsValidNew():
            cPasswordValid += 1
    return cPasswordValid

def Main():
    aryPassword = AryPasswordRead('2020/input/day_2.txt');
    print(CValidPasswordsOld(aryPassword))
    print(CValidPasswordsNew(aryPassword))

Main()