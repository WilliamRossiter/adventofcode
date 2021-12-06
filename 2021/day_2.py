
# https://adventofcode.com/2021/day/2

import common

def RunNavigation(aryStrDirection):
	x = 0
	z = 0
	for strDirection in aryStrDirection:
		instruction = strDirection.split()
		direction = instruction[0]
		cMagnitude = int(instruction[1])
		if (direction == 'forward'):
			x += cMagnitude
		elif (direction == 'up'):
			z -= cMagnitude
		elif (direction == 'down'):
			z += cMagnitude
	print(x)
	print(z)
	print(x * z)

def RunNavigationWithAim(aryStrDirection):
	aim = 0
	x = 0
	z = 0
	for strDirection in aryStrDirection:
		instruction = strDirection.split()
		direction = instruction[0]
		cMagnitude = int(instruction[1])
		if (direction == 'forward'):
			x += cMagnitude
			z += (cMagnitude * aim)
		elif (direction == 'up'):
			aim -= cMagnitude
		elif (direction == 'down'):
			aim += cMagnitude
	print(x)
	print(z)
	print(x * z)

def Main():
	aryStrDirection = common.AryStrFromFile('2021/input/day_2.txt')
	RunNavigation(aryStrDirection)
	RunNavigationWithAim(aryStrDirection)

Main()