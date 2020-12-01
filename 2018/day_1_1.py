
import fileinput

def ProcessFile():
    total = 0
    dict = {}
    while True:
        with fileinput.input(files=('input/day_1_1.txt')) as f:
            for line in f:
                total += int(line)
                key = "%d" % total
                inDict = dict.get(key)
                if inDict:
                    print(key)
                    return
                dict[key] = True

ProcessFile()