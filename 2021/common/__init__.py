
import fileinput

def AryNFromFile(strFile):
    aryN = []
    f = fileinput.input(files=(strFile))
    for line in f:
        aryN.append(int(line))
    f.close()
    return aryN