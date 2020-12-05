
# https://adventofcode.com/2020/day/2

import math
import common
import fileinput


# A password includes a definition of the rules that make that password valid,
#  namely a letter and the range of times that defines the rules of how many
#  instances of it can appear

class Password:
    
    def __init__(self, str):
        aryStrPassword = str.split()
        strRange = aryStrPassword[0]
        aryStrRange = strRange.split('-')
        self.m_cFirst = int(aryStrRange[0])
        self.m_cLast = int(aryStrRange[1])
        self.m_chLetter = aryStrPassword[1][0]
        self.strPassword = aryStrPassword[2]

    def FIsValidOld(self):
        cChRequired = 0
        for i in range(len(self.strPassword)):
            if self.strPassword[i] == self.m_chLetter:
                cChRequired += 1
        return cChRequired >= self.m_cFirst and cChRequired <= self.m_cLast

    def FIsValidNew(self):
        fMatchesFirst = self.strPassword[self.m_cFirst - 1] == self.m_chLetter
        fMatchesLast = self.strPassword[self.m_cLast - 1] == self.m_chLetter
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