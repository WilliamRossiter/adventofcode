import fileinput
import math

def ProcessFile():
    total = 0
    with fileinput.input(files=('input/day_1_1.txt')) as f:
        for line in f:
            module = int(line)
            fuel = GetFuelRequired(module)
            print(fuel)
            total += fuel
    print(total)

def GetFuelRequired(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel < 0:
        return 0
    else:
        return fuel + GetFuelRequired(fuel)


ProcessFile()