
import re
import enum
import copy

class Directions(enum.Enum):
    North = 0
    East = 1
    South = 2
    West = 3

    def OppositeDirection(direction):
        return Directions((direction.value + 2) % 4)

class Tile:
    def __init__(self, id, tileRows):
        self.id = id
        self.tileRows = tileRows
        self.tileNeighbors = {}
    
    def IsMatchingBorder(self, tileOther, direction):
        if direction == Directions.North:
            for i in range(len(self.tileRows)):
                borderPixelSelf = self.tileRows[0][i]
                borderPixelOther = tileOther.tileRows[len(self.tileRows) - 1][i]
                if borderPixelSelf != borderPixelOther:
                    return False
        elif direction == Directions.South:
            for i in range(len(self.tileRows)):
                borderPixelSelf = self.tileRows[len(self.tileRows) - 1][i]
                borderPixelOther = tileOther.tileRows[0][i]
                if borderPixelSelf != borderPixelOther:
                    return False
        elif direction == Directions.East:
            for i in range(len(self.tileRows)):
                borderPixelSelf = self.tileRows[i][len(self.tileRows) - 1]
                borderPixelOther = tileOther.tileRows[i][0]
                if borderPixelSelf != borderPixelOther:
                    return False
        elif direction == Directions.West:
            for i in range(len(self.tileRows)):
                borderPixelSelf = self.tileRows[i][0]
                borderPixelOther = tileOther.tileRows[i][len(self.tileRows) - 1]
                if borderPixelSelf != borderPixelOther:
                    return False
        return True
    
    def Flip(self):
        tileRowsNew = copy.deepcopy(self.tileRows)
        for i in range(len(self.tileRows)):
            for j in range(len(self.tileRows)):
                tileRowsNew[i][j] = self.tileRows[i][len(self.tileRows) - 1 - j]
        self.tileRows = tileRowsNew

    def Rotate(self):
        tileRowsNew = copy.deepcopy(self.tileRows)
        for i in range(len(self.tileRows)):
            for j in range(len(self.tileRows)):
                tileRowsNew[i][j] = self.tileRows[len(self.tileRows) - 1 - j][i]
        self.tileRows = tileRowsNew

    def TryMatchTileStatic(self, tileOther):
        for direction in (Directions):
            if self.tileNeighbors.get(direction) != None:
                continue
            elif tileOther.tileNeighbors.get(Directions.OppositeDirection(direction)) != None:
                continue
            elif self.IsMatchingBorder(tileOther, direction):
                self.tileNeighbors[direction] = tileOther
                tileOther.tileNeighbors[Directions.OppositeDirection(direction)] = self
                return True      

    def TryMatchTile(self, tileOther):
        for flip in range(2):
            for rotate in range(4):
                for direction in (Directions):
                    if self.tileNeighbors.get(direction) != None:
                        continue
                    elif tileOther.tileNeighbors.get(Directions.OppositeDirection(direction)) != None:
                        continue
                    elif self.IsMatchingBorder(tileOther, direction):
                        self.tileNeighbors[direction] = tileOther
                        tileOther.tileNeighbors[Directions.OppositeDirection(direction)] = self
                        return True
                tileOther.Rotate()
            tileOther.Flip()
        return False
    
    def RemoveBorders(self):
        self.tileRows.pop()
        self.tileRows.pop(0)
        for i in range(len(self.tileRows)):
            self.tileRows[i].pop()
            self.tileRows[i].pop(0)

class Input:
    def __init__(self, inputFile):
        self.tiles = []
        with open(inputFile) as f:
            inputTiles = f.read().split('\n\n')
            for inputTile in inputTiles:
                matchTileParts = re.match('Tile (\d+):\n([.#\n]+)', inputTile)
                id = matchTileParts[1]
                tileRowsRaw = matchTileParts[2]
                tileRows = []
                for tileRowRaw in tileRowsRaw.split():
                    tileRows.append(list(tileRowRaw))
                self.tiles.append(Tile(int(id), tileRows))

def BuildImage(tileTopLeft):
    tileRowStart = tileTopLeft
    tileCur = tileRowStart
    image = [[]]
    rowTile = 0
    rowImage = 0
    col = 0
    while True:
        if col >= len(tileCur.tileRows[rowTile]):
            tileCur = tileCur.tileNeighbors.get(Directions.East)
            col = 0
            if tileCur is None:
                tileCur = tileRowStart
                rowTile += 1
                rowImage += 1
                image.append([])
        if rowTile >= len(tileCur.tileRows):
            tileRowStart = tileRowStart.tileNeighbors.get(Directions.South)
            if tileRowStart is None:
                image.pop()
                return Tile(0, image)
            tileCur = tileRowStart
            rowTile = 0
        image[rowImage].append(tileCur.tileRows[rowTile][col])
        col += 1

def FindMatchesInImageStatic(image, imageToMatch):
    rowStart = 0
    colStart = 0
    matches = 0
    while True:
        if colStart >= len(image.tileRows[0]) - len(imageToMatch[0])+ 1:
            rowStart += 1
            colStart = 0
            if rowStart >= len(image.tileRows) - len(imageToMatch) + 1:
                return matches
        foundMatch = True
        for row in range(len(imageToMatch)):
            for col in range(len(imageToMatch[0])):
                if imageToMatch[row][col] != ' ' and image.tileRows[rowStart + row][colStart + col] != imageToMatch[row][col]:
                    foundMatch = False
                    break
            if not foundMatch:
                break
        if foundMatch:
            matches += 1
        colStart += 1

def FindMatchesInImage(image, imageToMatch):
    for flip in range(2):
        for rotate in range(4):
            matches = FindMatchesInImageStatic(image, imageToMatch)
            if matches > 0:
                return matches
            image.Rotate()
        image.Flip()
    return 0

def CountHashes(image):
    count = 0
    for row in image.tileRows:
        for col in row:
            if col == '#':
                count += 1
    return count
                    
input = Input('2020/input/day_20.txt')

matchedTiles = [input.tiles[0]]
tilesToMatch = [input.tiles[0]]

while len(tilesToMatch) > 0:
    tile = tilesToMatch.pop()
    for tileOther in input.tiles:
        if tileOther in matchedTiles:
            continue
        tile.TryMatchTile(tileOther)
    for tileMatched in tile.tileNeighbors.values():
        if tileMatched not in matchedTiles:
            matchedTiles.append(tileMatched)
            tilesToMatch.append(tileMatched)

for tile in matchedTiles:
    for tileOther in matchedTiles:
        if tile is tileOther:
            continue
        tile.TryMatchTileStatic(tileOther)

productCorners = 1

for tile in input.tiles:
    if len(tile.tileNeighbors) == 2:
        print(tile.id)
        productCorners *= tile.id

print(productCorners)

for tile in input.tiles:
    tile.RemoveBorders()

tileTopLeft = None

for tile in input.tiles:
    if tile.tileNeighbors.get(Directions.North) is None and tile.tileNeighbors.get(Directions.West) is None:
        tileTopLeft = tile
        break

image = BuildImage(tileTopLeft)

imageToMatch = [list('                  # '),list('#    ##    ##    ###'),list(' #  #  #  #  #  #   ')]

matches = FindMatchesInImage(image, imageToMatch)
print(CountHashes(image) - (matches * 15))