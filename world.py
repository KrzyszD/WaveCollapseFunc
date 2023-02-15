from config import width, height
from tile import Tile, tileTypes
from random import choice 
import time
import os

class World:


    def __init__(self):
        self.grid = []
        self.unfixedCoord = []

        for y in range(height):
            self.grid.append( [] )
            for x in range(width):
                self.grid[y].append( Tile(x, y) )
                self.unfixedCoord.append( (x, y) )
    
    def collapse(self):
        remaining = height * width

        while (remaining > 0):
            minEntropy = float('inf')
            minEntropyList = []

            for x, y in self.unfixedCoord:
                curTile = self.grid[y][x]
                if ( len(curTile.validTypes) < minEntropy ):
                    minEntropy = len(curTile.validTypes)
                    minEntropyList = [ (x, y) ]
                elif ( len(curTile.validTypes) == minEntropy ):
                    minEntropyList.append( (x, y) )

            if (minEntropy == 0):
                print("Failed")
                return

            x, y = choice( minEntropyList )
            curTile = self.grid[y][x]
            self.unfixedCoord.remove( (x, y) )

            tileType = choice(curTile.validTypes)
            # print(x, y, minEntropy)

            curTile.setType(tileType)

            self.collapseWave(x, y)

            remaining -= 1

            self.printWorld()
            os.system('cls')

    def collapseWave(self, x, y):

        queue = [(x, y)]

        while len(queue) > 0:
            x, y = queue.pop(0)

            curTile = self.grid[y][x]

            if (x > 0):
                # Left Neighbor
                validNeigh = curTile.getValidNeigh("left")
                
                neigh = self.grid[y][x - 1]

                if (neigh.checkCollapse(validNeigh)):
                    queue.append( (x-1, y) )

            if (x < width - 1):
                # right Neighbor
                validNeigh = curTile.getValidNeigh("right")
                
                neigh = self.grid[y][x + 1]

                if (neigh.checkCollapse(validNeigh)):
                    queue.append( (x+1, y) )

            if (y > 0):
                # top Neighbor
                validNeigh = curTile.getValidNeigh("top")
                
                neigh = self.grid[y - 1][x]

                if (neigh.checkCollapse(validNeigh)):
                    queue.append( (x, y - 1) )

            if (y < height - 1):
                # bottom Neighbor
                validNeigh = curTile.getValidNeigh("bottom")
                
                neigh = self.grid[y +  1][x]

                if (neigh.checkCollapse(validNeigh)):
                    queue.append( (x, y+1) )


    def printWorld(self, ASCII=True):

        for row in self.grid:
            for tile in row:
                if (ASCII) :
                    print(tileTypes[tile.type]["ascii"], end='')
                else:
                    pass
            print()