from tile import *
from config import *
from world import *
import os


if __name__ == "__main__":
    print("Wave Collapse")

    world = World()

    world.collapse()


    os.system('cls')
    world.printWorld()

    pass


