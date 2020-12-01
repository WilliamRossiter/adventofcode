import fileinput
import math

def ProcessFile():
    total = 0
    with fileinput.input(files=('input/day_1_1.txt')) as f:
        for line in f:
            module = int(line)
            print(module)
            fuel = math.floor(module / 3) - 2
            total += fuel
    print(total)

ProcessFile()