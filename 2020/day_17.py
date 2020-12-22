
def GenerateCombos(values, size):
    combosOuter = []
    if (size == 1):
        for value in values:
            combosOuter.append([value])
    else:
        for value in values:
            combosInner = GenerateCombos(values, size - 1)
            for combo in combosInner:
                combosOuter.append(combo)
                combosOuter[-1].append(value)
    return combosOuter

class Input:
    def __init__(self, strFile):
        self.pocketDimension = PocketDimension()
        with open(strFile) as f:
            x = 0
            for line in f:
                y = 0
                for ch in line:
                    z = 0
                    w = 0
                    if ch == '.':
                        self.pocketDimension.SetValueAt(x, y, z, w, 0)
                    elif ch == '#':
                        self.pocketDimension.SetValueAt(x, y, z, w, 1)
                    y += 1
                x += 1

class PocketDimension:
    def __init__(self):
        self.xyzwCoord = {}
        self.rangeX = (0, 0)
        self.rangeY = (0, 0)
        self.rangeZ = (0, 0)
        self.rangeW = (0, 0)
        
    def GetValueAt(self, x, y, z, w):
        yzwCoord = self.xyzwCoord.get(x)
        if (yzwCoord == None):
            return 0
        zwCoord = yzwCoord.get(y)
        if zwCoord == None:
            return 0
        wCoord = zwCoord.get(z)
        if wCoord == None:
            return 0
        value = wCoord.get(w)
        if value == None:
            return 0
        else:
            return value

    def SetValueAt(self, x, y, z, w, value):
        yzwCoord = self.xyzwCoord.get(x)
        if yzwCoord == None:
            self.xyzwCoord[x] = {}
            yzwCoord = self.xyzwCoord[x]
        zwCoord = yzwCoord.get(y)
        if zwCoord == None:
            yzwCoord[y] = {}
            zwCoord = yzwCoord[y]
        wCoord = zwCoord.get(z)
        if wCoord == None:
            zwCoord[z] = {}
            wCoord = zwCoord[z]
        wCoord[w] = value
        self.rangeX = (min(x, self.rangeX[0]), max(x + 1, self.rangeX[1]))
        self.rangeY = (min(y, self.rangeY[0]), max(y + 1, self.rangeY[1]))
        self.rangeZ = (min(z, self.rangeZ[0]), max(z + 1, self.rangeZ[1]))
        self.rangeW = (min(w, self.rangeW[0]), max(w + 1, self.rangeW[1]))

    def GetNumActive(self):
        numActive = 0
        for x in self.xyzwCoord.keys():
            for y in self.xyzwCoord[x].keys():
                for z in self.xyzwCoord[x][y].keys():
                    for w in self.xyzwCoord[x][y][z].keys():
                        if self.xyzwCoord[x][y][z][w] == 1:
                            numActive += 1
        return numActive

def Process(pocketDimension, x, y, z, w, combos, pocketDimensionNew):
    value = pocketDimension.GetValueAt(x, y, z, w)
    neighborsOn = 0
    for combo in combos:
        xNeighbor = x + combo[0]
        yNeighbor = y + combo[1]
        zNeighbor = z + combo[2]
        wNeighbor = w + combo[3]
        valueNeighbor = pocketDimension.GetValueAt(xNeighbor, yNeighbor, zNeighbor, wNeighbor)
        neighborsOn += valueNeighbor
    if value == 1:
        if neighborsOn == 2 or neighborsOn == 3:
            value = 1
        else:
            value = 0
    elif neighborsOn == 3:
        value = 1
    pocketDimensionNew.SetValueAt(x, y, z, w, value)

def RunCycles(pocketDimension, cycles):
    combos = GenerateCombos([-1, 0, 1], 4)
    combos.remove([0,0,0,0])
    for cycle in range(cycles):
        pocketDimensionNew = PocketDimension()
        for x in range(pocketDimension.rangeX[0] - 1, pocketDimension.rangeX[1] + 1):
            for y in range(pocketDimension.rangeY[0] - 1, pocketDimension.rangeY[1] + 1):
                for z in range(pocketDimension.rangeZ[0] - 1, pocketDimension.rangeZ[1] + 1):
                    for w in range(pocketDimension.rangeW[0] - 1, pocketDimension.rangeW[1] + 1):
                        Process(pocketDimension, x, y, z, w, combos, pocketDimensionNew)
        pocketDimension = pocketDimensionNew
    return pocketDimension


input = Input('2020/input/day_17.txt')
pocketDimension = RunCycles(input.pocketDimension, 6)
print(pocketDimension.GetNumActive())