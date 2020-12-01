
# https://adventofcode.com/2020/day/1

import math
import common



# Gets a list of numbers from the input with length cN that has the sum of nSum

def FGetSubArrayWithSum(aryN, cN, nSum, aryNFinal):
    if cN == 1:
        for n in aryN:
            if n == nSum:
                aryNFinal.append(n)
                return True
    else:
        for i in range(len(aryN)):
            aryNOther = list(aryN)
            n = aryNOther.pop(i)
            if FGetSubArrayWithSum(aryNOther, cN - 1, nSum - n, aryNFinal):
                aryNFinal.append(n)
                return True
    return False

# Returns the product of the numbers returned by FGetSubArrayWithSum

def NProductOfIntegerSubsetWithSum(aryN, cN, nSum):
    aryNFinal = []
    if FGetSubArrayWithSum(aryN, cN, nSum, aryNFinal):
        nProduct = 1
        for n in aryNFinal:
            nProduct *= n
        return nProduct
    else:
        print('Could not find %d numbers that summed to %d' % (cN, nSum))
        return 0

def PrintProductOfNumbersWithSum(aryN, cN, nSum):
    print(NProductOfIntegerSubsetWithSum(aryNInput, cN, nSum))

def Main():
    aryNInput = common.AryNFromFile('2020/input/day_1.txt')
    print(NProductOfIntegerSubsetWithSum(aryNInput, 2, 2020))
    print(NProductOfIntegerSubsetWithSum(aryNInput, 3, 2020))

Main()