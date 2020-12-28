
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
    dimensions = 10
    def __init__(self, id, tileRows):
        self.id = id
        self.tileRows = tileRows
        self.tileNeighbors = {}
    
    def IsMatchingBorder(self, tileOther, direction):
        if direction == Directions.North:
            for i in range(Tile.dimensions):
                borderPixelSelf = self.tileRows[0][i]
                borderPixelOther = tileOther.tileRows[Tile.dimensions - 1][i]
                if borderPixelSelf != borderPixelOther:
                    return False
        elif direction == Directions.South:
            for i in range(Tile.dimensions):
                borderPixelSelf = self.tileRows[Tile.dimensions - 1][i]
                borderPixelOther = tileOther.tileRows[0][i]
                if borderPixelSelf != borderPixelOther:
                    return False
        elif direction == Directions.East:
            for i in range(Tile.dimensions):
                borderPixelSelf = self.tileRows[i][Tile.dimensions - 1]
                borderPixelOther = tileOther.tileRows[i][0]
                if borderPixelSelf != borderPixelOther:
                    return False
        elif direction == Directions.West:
            for i in range(Tile.dimensions):
                borderPixelSelf = self.tileRows[i][0]
                borderPixelOther = tileOther.tileRows[i][Tile.dimensions - 1]
                if borderPixelSelf != borderPixelOther:
                    return False
        return True
    
    def Flip(self):
        tileRowsNew = copy.deepcopy(self.tileRows)
        for i in range(Tile.dimensions):
            for j in range(Tile.dimensions):
                tileRowsNew[i][j] = self.tileRows[i][Tile.dimensions - 1 - j]
        self.tileRows = tileRowsNew

    def Rotate(self):
        tileRowsNew = copy.deepcopy(self.tileRows)
        for i in range(Tile.dimensions):
            for j in range(Tile.dimensions):
                tileRowsNew[i][j] = self.tileRows[Tile.dimensions - 1 - j][i]
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