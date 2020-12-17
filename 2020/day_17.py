
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
        self.grid = []
        with open(strFile) as f:
            for line in f:
                row = []
                self.grid.append(row)
                for ch in line:
                    if ch == '.':
                        row.append(0)
                    elif ch == '#':
                        row.append(1)

def Process(grid, row, col, combos):
    for combo in combos:
        

def RunCycles(grid, cycles):
    combos = GenerateCombos([-1, 0, 1], 3)
    combos.remove([0,0,0])
    for cycle in range(cycles):
        newGrid = []
        for row in grid:
            newRow = []
            newGrid.append(newRow)
            for col in row:
                newRow.append(Process(grid, row, col, combos))
        grid = newGrid


input = Input('2020/input/day_17.txt')
RunCycles(input.grid, 6)