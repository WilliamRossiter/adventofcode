
import common

class Schematic:
    def __init__(self, file):
        lines = common.AryStrFromFile(file)
        self.width = len(lines[0])
        self.data = []
        self.schemeNumbers = []
        self.schemeSymbols = []
        for line in lines:
            for char in line:
                self.data.append(char)
        isReadingSchematicNumber = False
        number = 0
        row = 0
        colStart = 0
        colEnd = 0
        for index, char in enumerate(self.data):
            if index % self.width == 0:
                    if isReadingSchematicNumber:
                        isReadingSchematicNumber = False
                        schemeNumber = SchematicNumber(self, number, row, colStart, colEnd)
                        self.schemeNumbers.append(schemeNumber)                            
            if (char.isdigit()):
                if isReadingSchematicNumber:
                    number = (number * 10) + int(char)
                    colEnd = index % self.width
                else:
                    isReadingSchematicNumber = True
                    number = int(char)
                    row = int(index / self.width)
                    colStart = index % self.width
                    colEnd = colStart
            elif isReadingSchematicNumber:
                isReadingSchematicNumber = False
                schemeNumber = SchematicNumber(self, number, row, colStart, colEnd)
                self.schemeNumbers.append(schemeNumber)
            if (char == "*"):
                row = int(index / self.width)
                col = index % self.width
                schemeSymbol = SchematicSymbol(self, number, row, col)
                self.schemeSymbols.append(schemeSymbol)

    def Get(self, row, col):
        index = int(row * self.width + col)
        if index < 0 or index >= len(self.data):
            return '.'
        else:
            return self.data[index]
        
    def GetSchemeNumber(self, row, col):
        for schemeNumber in self.schemeNumbers:
            if (schemeNumber.row == row and schemeNumber.colStart <= col and schemeNumber.colEnd >= col):
                return schemeNumber
        return None

class SchematicNumber:
    def __init__(self, schematic, number, row, colStart, colEnd):
        self.schematic = schematic
        self.number = number
        self.row = row
        self.colStart = colStart
        self.colEnd = colEnd

    def isPartNumber(self):
        colCur = self.colStart
        while colCur <= self.colEnd:
            for spot in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                char = self.schematic.Get(self.row + spot[0], colCur + spot[1])
                if char != '.' and not char.isdigit():
                    return True
            colCur += 1
        return False
    
class SchematicSymbol:
    def __init__(self, schematic, number, row, col):
        self.schematic = schematic
        self.number = number
        self.row = row
        self.col = col

    def gearRatio(self):
        schemeNumber1 = None
        schemeNumber2 = None
        for spot in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            schemeNumber = self.schematic.GetSchemeNumber(self.row + spot[0], self.col + spot[1])
            if (schemeNumber):
                if schemeNumber is schemeNumber1 or schemeNumber is schemeNumber2:
                    continue
                if not schemeNumber1:
                    schemeNumber1 = schemeNumber
                elif not schemeNumber2:
                    schemeNumber2 = schemeNumber
                else:
                    return 0
        if schemeNumber1 and schemeNumber2:
            return schemeNumber1.number * schemeNumber2.number
        else:
            return 0
        
def Main():
    schematic = Schematic('2023/input/day_3.txt')
    theSumOfAllParts = 0
    for schemeNumber in schematic.schemeNumbers:
        if schemeNumber.isPartNumber():
            theSumOfAllParts += schemeNumber.number
        else:
            print(schemeNumber.number)
    print(theSumOfAllParts)
    theSumOfAllGears = 0
    for schemeSymbol in schematic.schemeSymbols:
        theSumOfAllGears += schemeSymbol.gearRatio()
    print(theSumOfAllGears)

Main()