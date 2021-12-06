
# https://adventofcode.com/2021/day/3

import common

def NFromAryBit(aryBit):
	n = 0
	cBit = len(aryBit)
	for iBit in range(cBit):
		if aryBit[iBit] == 1:
			n += pow(2, (cBit - iBit - 1))
	return n

def NMostCommonBit(aryStrBinary, iPosition):
	cZero = 0
	cOne = 0
	for strBinary in aryStrBinary:
		if (strBinary[iPosition] == "0"):
			cZero += 1
		else:
			cOne += 1
	if (cZero > cOne):
		return 0
	else:
		return 1

def NGammaRate(aryStrPowerConsumption):
	cBit = len(aryStrPowerConsumption[0])
	aryBit = []
	for iBit in range(cBit):
		aryBit.append(NMostCommonBit(aryStrPowerConsumption, iBit))
	print(aryBit)
	return NFromAryBit(aryBit)

def NEpsilonRate(aryStrPowerConsumption):
	cBit = len(aryStrPowerConsumption[0])
	aryBit = []
	for iBit in range(cBit):
		aryBit.append(1 - NMostCommonBit(aryStrPowerConsumption, iBit))
	print(aryBit)
	return NFromAryBit(aryBit)

def Main():
	aryStrPowerConsumption = common.AryStrFromFile('2021/input/day_3.txt')
	nGammaRate = NGammaRate(aryStrPowerConsumption)
	nEpsilonRate = NEpsilonRate(aryStrPowerConsumption)
	print(nGammaRate)
	print(nEpsilonRate)
	print(nGammaRate * nEpsilonRate)

Main()