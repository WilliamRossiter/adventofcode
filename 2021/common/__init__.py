
import fileinput

def AryNFromFile(strFile):
    aryN = []
    f = fileinput.input(files=(strFile))
    for line in f:
        aryN.append(int(line))
    f.close()
    return aryN

def AryStrFromFile(strFile):
    aryStr = []
    f = open(strFile, 'r')
    input = f.read()
    return input.splitlines()