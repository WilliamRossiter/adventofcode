
# https://adventofcode.com/2021/day/1

import common

def CDepthIncrease(aryN):
	cDepthIncrease = 0
	nDepthLast = aryN[0]
	for i in range(1, len(aryN)):
		if nDepthLast >= 0 and aryN[i] > nDepthLast:
			cDepthIncrease += 1
		nDepthLast = aryN[i]
	return cDepthIncrease

def CDepthIncreaseSum3(aryN):
	cDepthIncrease = 0
	nSumLast = aryN[0] + aryN[1] + aryN[2]
	for i in range(3, len(aryN)):
		nSumCur = nSumLast - aryN[i - 3] + aryN[i]
		if nSumCur > nSumLast:
			cDepthIncrease += 1
		nSumLast = nSumCur
	return cDepthIncrease

def Main():
	aryNInput = common.AryNFromFile('2021/input/day_1.txt')
	print(CDepthIncrease(aryNInput))
	print(CDepthIncreaseSum3(aryNInput))

Main()