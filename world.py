from config import width, height, mode
from tile import Tile, tileTypes
from random import choice, choices
import numpy as np
import time
import os

class World:


    def __init__(self):
        self.grid = []
        self.unfixedCoord = []

        # Initiliaze all tiles
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

            # Find tile with least entropy (least tile choices)
            for x, y in self.unfixedCoord:
                curTile = self.grid[y][x]
                if ( len(curTile.validTypes) < minEntropy ):
                    minEntropy = len(curTile.validTypes)
                    minEntropyList = [ (x, y) ]
                elif ( len(curTile.validTypes) == minEntropy ):
                    minEntropyList.append( (x, y) )

            # If tile has zero choices, exit gracefully
            if (minEntropy == 0):
                print("Failed")
                return

            # Choose random tile with minimum entropy
            x, y = choice( minEntropyList )
            curTile = self.grid[y][x]
            self.unfixedCoord.remove( (x, y) )

            # Choose random valid type
            tileType = self.chooseTile(x, y)
            curTile.setType(tileType)

            # Collapse neighboring tiles
            self.collapseWave(x, y)

            remaining -= 1

            # Show progress, optional
            os.system('cls')
            self.printWorld()

    def chooseTile(self, x, y):
        curTile = self.grid[y][x]
        
        if mode < 4:
            return choice(curTile.validTypes)
        
        weights = np.ones( (len(curTile.validTypes)) )
        
        
        if (x > 0):
            # Left Neighbor            
            neigh = self.grid[y][x - 1]

            if neigh.determined:
                neighWeights = tileTypes[neigh.type]["rightWeights"]

                for i in range(len(curTile.validTypes)):
                    if curTile.validTypes[i] in neighWeights:
                        weights[i] *= neighWeights[curTile.validTypes[i]]

        if (x < width - 1):
            # right Neighbor
            neigh = self.grid[y][x + 1]

            if neigh.determined:
                neighWeights = tileTypes[neigh.type]["leftWeights"]

                for i in range(len(curTile.validTypes)):
                    if curTile.validTypes[i] in neighWeights:
                        weights[i] *= neighWeights[curTile.validTypes[i]]

        if (y > 0):
            # top Neighbor
            neigh = self.grid[y - 1][x]

            if neigh.determined:
                neighWeights = tileTypes[neigh.type]["bottomWeights"]

                for i in range(len(curTile.validTypes)):
                    if curTile.validTypes[i] in neighWeights:
                        weights[i] *= neighWeights[curTile.validTypes[i]]

        if (y < height - 1):
            # bottom Neighbor
            neigh = self.grid[y +  1][x]

            if neigh.determined:
                neighWeights = tileTypes[neigh.type]["topWeights"]

                for i in range(len(curTile.validTypes)):
                    if curTile.validTypes[i] in neighWeights:
                        weights[i] *= neighWeights[curTile.validTypes[i]]
        
        c = choices(curTile.validTypes, weights=weights)

        return c[0]

    def collapseWave(self, x, y):

        # Queue of updated restricted tiles
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
        # Prints world
        for row in self.grid:
            for tile in row:
                if (ASCII) :
                    print(tileTypes[tile.type]["ascii"], end='')
                else:
                    pass
            print()