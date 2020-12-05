
# https://adventofcode.com/2020/day/4

import math
import common
import fileinput

class Passport:
    def __init__(self, str):
        self.m_dict = {}
        aryStrKv = str.split()
        for strKv in aryStrKv:
            kv = strKv.split(":")
            self.m_dict[kv[0]] = kv[1]

    def FIsValid(self, dictFieldValidation):
        for strKey in dictFieldValidation.keys():
            if strKey in self.m_dict:
                if not dictFieldValidation[strKey](self.m_dict[strKey]):
                    print self.m_dict[strKey]
                    return False
            else:
                return False
        return True

def range1(start, end):
    return range(start, end + 1)

def AryPassportRead(strFile):
    aryPassport = []
    with open(strFile) as f:
        strInput = f.read()
        aryStrPassport = strInput.split("\n\n")
        for strPassport in aryStrPassport:
            aryPassport.append(Passport(strPassport))
    return aryPassport

def CValidPassports(aryPassport, dictFieldValidation):
    cValid = 0
    for passport in aryPassport:
        if passport.FIsValid(dictFieldValidation):
            cValid += 1
    return cValid

def FIsValidBirthYear(strBirthYear):
    if len(strBirthYear) != 4:
        return False
    else:
        return int(strBirthYear) in range1(1920, 2002)

def FIsValidIssueYear(strIssueYear):
    if len(strIssueYear) != 4:
        return False
    else:
        return int(strIssueYear) in range1(2010, 2020)

def FIsValidExpirationYear(strExpirationYear):
    if len(strExpirationYear) != 4:
        return False
    else:
        return int(strExpirationYear) in range1(2020, 2030)

def FIsValidHeight(strHeight):
    strHeightInches = strHeight.split("in")
    strHeightCentimeters = strHeight.split("cm")
    if strHeightInches[0] != strHeight:
        return int(strHeightInches[0]) in range1(59, 76)
    elif strHeightCentimeters[0] != strHeight:
       return int(strHeightCentimeters[0]) in range1(150, 193)
    else:
        return False

def FIsValidHairColor(strHairColor):
    if len(strHairColor) != 7:
        return False
    elif strHairColor[0] != '#':
        return False
    else:
        for iCh in range(1, len(strHairColor)):
            ch = strHairColor[iCh]
            if ch.isdigit():
                if int(ch) not in range1(0, 9):
                    return False
            elif ch.isalpha:
                if ch not in "abcdef":
                    return False
    return True

def FIsValidEyeColor(strEyeColor):
    return strEyeColor in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def FIsValidPassportId(strPassportId):
    return strPassportId.isdigit() and len(strPassportId) == 9

def Main():
    strFile = '2020/input/day_4.txt'
    dictFieldValidation = {
        "byr": FIsValidBirthYear,
        "iyr": FIsValidIssueYear,
        "eyr": FIsValidExpirationYear,
        "hgt": FIsValidHeight,
        "hcl": FIsValidHairColor,
        "ecl": FIsValidEyeColor,
        "pid": FIsValidPassportId
    }
    aryPassport = AryPassportRead(strFile)
    print(CValidPassports(aryPassport, dictFieldValidation))

Main()