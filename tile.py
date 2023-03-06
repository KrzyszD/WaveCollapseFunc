from config import mode

class Tile:

    directions = ["right", "left", "top", "bottom"]

    def __init__(self, x, y):
        # If type is determined and type
        self.determined = False 
        self.type = ""

        # List of types that are valid
        self.validTypes = list(tileTypes.keys()) 
        self.validTypes.remove("")

        # Coordinates of tile
        self.x = x
        self.y = y

    def setType(self, type):
        self.determined = True
        self.type = type
        self.validTypes = [ type ]
    
    def getValidNeigh(self, direction):
        # Get list of valid neighbor types in a given direction based on current valid types
        neigh = set()

        # Go through all potential tile types
        for validType in self.validTypes:
            # Add potential neighbor types
            # print()
            # print(validType)
            # print(tileTypes[validType])
            # print(tileTypes[validType][direction])
            # print()
            neigh = neigh.union( set(tileTypes[validType][direction]) )

        return list(neigh)

    def checkCollapse(self, potentialTypes):
        # Check if change in neighbor restricts this tiles validTypes
        # If yes, then restrict and return True,
        # Else, then return False

        if (self.determined):
            return False

        validTypes = set(self.validTypes)
        potentialTypes = set(potentialTypes)

        subset = validTypes.issubset( potentialTypes )

        if ( subset ):
            # potentialTypes does not restrict
            return False

        # potentialTypes does restrict
        # Restrict validTypes
        self.validTypes = list( validTypes & potentialTypes )

        return True
    

    
if mode == 0:
    tileTypes = {

        "" : 
        {
            "name" : "",
            "png" : "",
            "ascii" : "○",
            "right" : [""],
            "left" : [""],
            "top" : [""],
            "bottom" : [""]
        },

        "floor" : 
        {
            "name" : "floor",
            "png" : "",
            "ascii" : " ",
            "right" : ["floor", "wall_right"],
            "left" : ["floor", "wall_left"],
            "top" : ["floor", "wall_top"],
            "bottom" : ["floor", "wall_bottom"]
        },

        "solid" : 
        {
            "name" : "solid",
            "png" : "",
            "ascii" : "█",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "wall_right" : 
        {
            "name" : "wall_right",
            "png" : "",
            "ascii" : "║",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright"],
            "bottom" : ["wall_right", "corner_bottomright"]
        },

        "wall_left" : 
        {
            "name" : "wall_left",
            "png" : "",
            "ascii" : "║",
            "right" : ["floor"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["wall_left", "corner_topleft"],
            "bottom" : ["wall_left", "corner_bottomleft"]
        },

        "wall_top" : 
        {
            "name" : "wall_top",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_top", "corner_topright"],
            "left" : ["wall_top", "corner_topleft"],
            "top" : ["wall_bottom", "solid", "corner_bottomleft", "corner_bottomright"],
            "bottom" : ["floor"]
        },

        "wall_bottom" : 
        {
            "name" : "wall_bottom",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_bottom", "corner_bottomright"],
            "left" : ["wall_bottom", "corner_bottomleft"],
            "top" : ["floor"],
            "bottom" : ["wall_top", "solid", "corner_topleft", "corner_topright"]
        },

        "corner_topright" : 
        {
            "name" : "corner_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["wall_top"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["wall_right"]
        },

        "corner_topleft" : 
        {
            "name" : "corner_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_top"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["wall_left"]
        },

        "corner_bottomright" : 
        {
            "name" : "corner_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["wall_bottom"],
            "top" : ["wall_right"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "corner_bottomleft" : 
        {
            "name" : "corner_bottomleft",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_bottom"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["wall_left"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        }

    }
elif mode == 1:
    tileTypes = {

        "" : 
        {
            "name" : "",
            "png" : "",
            "ascii" : "○",
            "right" : [""],
            "left" : [""],
            "top" : [""],
            "bottom" : [""]
        },

        "floor" : 
        {
            "name" : "floor",
            "png" : "",
            "ascii" : " ",
            "right" : ["floor", "wall_right", "invert_bottomleft", "invert_topleft"],
            "left" : ["floor", "wall_left", "invert_bottomright", "invert_topright"],
            "top" : ["floor", "wall_top", "invert_bottomright", "invert_bottomleft"],
            "bottom" : ["floor", "wall_bottom", "invert_topright", "invert_topleft"]
        },

        "solid" : 
        {
            "name" : "solid",
            "png" : "",
            "ascii" : "█",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "wall_right" : 
        {
            "name" : "wall_right",
            "png" : "",
            "ascii" : "║",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright", "invert_topleft"],
            "bottom" : ["wall_right", "corner_bottomright", "invert_bottomleft"]
        },

        "wall_left" : 
        {
            "name" : "wall_left",
            "png" : "",
            "ascii" : "║",
            "right" : ["floor"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["wall_left", "corner_topleft", "invert_topright"],
            "bottom" : ["wall_left", "corner_bottomleft", "invert_bottomright"]
        },

        "wall_top" : 
        {
            "name" : "wall_top",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_top", "corner_topright", "invert_bottomright"],
            "left" : ["wall_top", "corner_topleft", "invert_bottomleft"],
            "top" : ["wall_bottom", "solid", "corner_bottomleft", "corner_bottomright"],
            "bottom" : ["floor"]
        },

        "wall_bottom" : 
        {
            "name" : "wall_bottom",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_bottom", "corner_bottomright", "invert_topleft"],
            "left" : ["wall_bottom", "corner_bottomleft", "invert_topright"],
            "top" : ["floor"],
            "bottom" : ["wall_top", "solid", "corner_topleft", "corner_topright"]
        },

        "corner_topright" : 
        {
            "name" : "corner_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["wall_top", "invert_bottomleft"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["wall_right", "invert_bottomleft"]
        },

        "corner_topleft" : 
        {
            "name" : "corner_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_top", "invert_bottomright"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["wall_left", "invert_bottomright"]
        },

        "corner_bottomright" : 
        {
            "name" : "corner_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["wall_bottom", "invert_topleft"],
            "top" : ["wall_right", "invert_topleft"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "corner_bottomleft" : 
        {
            "name" : "corner_bottomleft",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_bottom", "invert_topright"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["wall_left", "invert_topright"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "invert_topright" : 
        {
            "name" : "invert_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["floor"],
            "left" : ["wall_bottom", "corner_bottomleft", "invert_topleft"],
            "top" : ["floor"],
            "bottom" : ["wall_left", "corner_bottomleft", "invert_bottomright"]
        },

        "invert_topleft" : 
        {
            "name" : "invert_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_bottom", "corner_bottomright", "invert_topright"],
            "left" : ["floor"],
            "top" : ["floor"],
            "bottom" : ["wall_right", "corner_bottomright", "invert_bottomleft"]
        },

        "invert_bottomright" : 
        {
            "name" : "invert_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["floor"],
            "left" : ["wall_top", "corner_topleft", "invert_bottomleft"],
            "top" : ["wall_left", "corner_topleft", "invert_topright"],
            "bottom" : ["floor"]
        },

        "invert_bottomleft" : 
        {
            "name" : "invert_bottomright",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_top", "corner_topright", "invert_bottomright"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright", "invert_topleft"],
            "bottom" : ["floor"]
        }

    }
elif mode == 2:
    tileTypes = {

        "" : 
        {
            "name" : "",
            "png" : "",
            "ascii" : "○",
            "right" : [""],
            "left" : [""],
            "top" : [""],
            "bottom" : [""]
        },

        "floor" : 
        {
            "name" : "floor",
            "png" : "",
            "ascii" : " ",
            "right" : ["floor", "wall_right", "invert_bottomleft", "invert_topleft"],
            "left" : ["floor", "wall_left", "invert_bottomright", "invert_topright"],
            "top" : ["floor", "wall_top", "invert_bottomright", "invert_bottomleft"],
            "bottom" : ["floor", "wall_bottom", "invert_topright", "invert_topleft"]
        },

        "solid" : 
        {
            "name" : "solid",
            "png" : "",
            "ascii" : "█",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "wall_right" : 
        {
            "name" : "wall_right",
            "png" : "",
            "ascii" : "║",
            "right" : ["solid"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright", "invert_topleft"],
            "bottom" : ["wall_right", "corner_bottomright", "invert_bottomleft"]
        },

        "wall_left" : 
        {
            "name" : "wall_left",
            "png" : "",
            "ascii" : "║",
            "right" : ["floor"],
            "left" : ["solid"],
            "top" : ["wall_left", "corner_topleft", "invert_topright"],
            "bottom" : ["wall_left", "corner_bottomleft", "invert_bottomright"]
        },

        "wall_top" : 
        {
            "name" : "wall_top",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_top", "corner_topright", "invert_bottomright"],
            "left" : ["wall_top", "corner_topleft", "invert_bottomleft"],
            "top" : ["solid"],
            "bottom" : ["floor"]
        },

        "wall_bottom" : 
        {
            "name" : "wall_bottom",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_bottom", "corner_bottomright", "invert_topright"],
            "left" : ["wall_bottom", "corner_bottomleft", "invert_topleft"],
            "top" : ["floor"],
            "bottom" : ["solid"]
        },

        "corner_topright" : 
        {
            "name" : "corner_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["solid"],
            "left" : ["wall_top", "invert_bottomleft"],
            "top" : ["solid"],
            "bottom" : ["wall_right", "invert_bottomleft"]
        },

        "corner_topleft" : 
        {
            "name" : "corner_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_top", "invert_bottomright"],
            "left" : ["solid"],
            "top" : ["solid"],
            "bottom" : ["wall_left", "invert_bottomright"]
        },

        "corner_bottomright" : 
        {
            "name" : "corner_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["solid"],
            "left" : ["wall_bottom", "invert_topleft"],
            "top" : ["wall_right", "invert_topleft"],
            "bottom" : ["solid"]
        },

        "corner_bottomleft" : 
        {
            "name" : "corner_bottomleft",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_bottom", "invert_topright"],
            "left" : ["solid"],
            "top" : ["wall_left", "invert_topright"],
            "bottom" : ["solid"]
        },

        "invert_topright" : 
        {
            "name" : "invert_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["floor"],
            "left" : ["wall_bottom", "corner_bottomleft", "invert_topleft"],
            "top" : ["floor"],
            "bottom" : ["wall_left", "corner_bottomleft", "invert_bottomright"]
        },

        "invert_topleft" : 
        {
            "name" : "invert_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_bottom", "corner_bottomright", "invert_topright"],
            "left" : ["floor"],
            "top" : ["floor"],
            "bottom" : ["wall_right", "corner_bottomright", "invert_bottomleft"]
        },

        "invert_bottomright" : 
        {
            "name" : "invert_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["floor"],
            "left" : ["wall_top", "corner_topleft", "invert_bottomleft"],
            "top" : ["wall_left", "corner_topleft", "invert_topright"],
            "bottom" : ["floor"]
        },

        "invert_bottomleft" : 
        {
            "name" : "invert_bottomleft",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_top", "corner_topright", "invert_bottomright"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright", "invert_topleft"],
            "bottom" : ["floor"]
        }

    }
elif mode == 3:
    tileTypes = {

        "" : 
        {
            "name" : "",
            "png" : "",
            "ascii" : "○",
            "right" : [""],
            "left" : [""],
            "top" : [""],
            "bottom" : [""]
        },

        "floor" : 
        {
            "name" : "floor",
            "png" : "",
            "ascii" : " ",
            "right" : ["floor", "wall_right", "invert_bottomleft", "invert_topleft"],
            "left" : ["floor", "wall_left", "invert_bottomright", "invert_topright"],
            "top" : ["floor", "wall_top", "invert_bottomright", "invert_bottomleft"],
            "bottom" : ["floor", "wall_bottom", "invert_topright", "invert_topleft"]
        },

        "solid" : 
        {
            "name" : "solid",
            "png" : "",
            "ascii" : "█",
            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"]
        },

        "wall_right" : 
        {
            "name" : "wall_right",
            "png" : "",
            "ascii" : "║",
            "right" : ["solid"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright", "invert_topleft"],
            "bottom" : ["wall_right", "corner_bottomright", "invert_bottomleft"]
        },

        "wall_left" : 
        {
            "name" : "wall_left",
            "png" : "",
            "ascii" : "║",
            "right" : ["floor"],
            "left" : ["solid"],
            "top" : ["wall_left", "corner_topleft", "invert_topright"],
            "bottom" : ["wall_left", "corner_bottomleft", "invert_bottomright"]
        },

        "wall_top" : 
        {
            "name" : "wall_top",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_top", "corner_topright", "invert_bottomright"],
            "left" : ["wall_top", "corner_topleft", "invert_bottomleft"],
            "top" : ["solid"],
            "bottom" : ["floor"]
        },

        "wall_bottom" : 
        {
            "name" : "wall_bottom",
            "png" : "",
            "ascii" : "═",
            "right" : ["wall_bottom", "corner_bottomright", "invert_topright"],
            "left" : ["wall_bottom", "corner_bottomleft", "invert_topleft"],
            "top" : ["floor"],
            "bottom" : ["solid"]
        },

        "corner_topright" : 
        {
            "name" : "corner_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["solid"],
            "left" : ["wall_top", "invert_bottomleft"],
            "top" : ["solid"],
            "bottom" : ["wall_right", "invert_bottomleft"]
        },

        "corner_topleft" : 
        {
            "name" : "corner_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_top", "invert_bottomright"],
            "left" : ["solid"],
            "top" : ["solid"],
            "bottom" : ["wall_left", "invert_bottomright"]
        },

        "corner_bottomright" : 
        {
            "name" : "corner_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["solid"],
            "left" : ["wall_bottom", "invert_topleft"],
            "top" : ["wall_right", "invert_topleft"],
            "bottom" : ["solid"]
        },

        "corner_bottomleft" : 
        {
            "name" : "corner_bottomleft",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_bottom", "invert_topright"],
            "left" : ["solid"],
            "top" : ["wall_left", "invert_topright"],
            "bottom" : ["solid"]
        },

        "invert_topright" : 
        {
            "name" : "invert_topright",
            "png" : "",
            "ascii" : "╗",
            "right" : ["floor"],
            "left" : ["wall_bottom", "corner_bottomleft"],
            "top" : ["floor"],
            "bottom" : ["wall_left", "corner_bottomleft"]
        },

        "invert_topleft" : 
        {
            "name" : "invert_topleft",
            "png" : "",
            "ascii" : "╔",
            "right" : ["wall_bottom", "corner_bottomright"],
            "left" : ["floor"],
            "top" : ["floor"],
            "bottom" : ["wall_right", "corner_bottomright"]
        },

        "invert_bottomright" : 
        {
            "name" : "invert_bottomright",
            "png" : "",
            "ascii" : "╝",
            "right" : ["floor"],
            "left" : ["wall_top", "corner_topleft"],
            "top" : ["wall_left", "corner_topleft"],
            "bottom" : ["floor"]
        },

        "invert_bottomleft" : 
        {
            "name" : "invert_bottomleft",
            "png" : "",
            "ascii" : "╚",
            "right" : ["wall_top", "corner_topright"],
            "left" : ["floor"],
            "top" : ["wall_right", "corner_topright"],
            "bottom" : ["floor"]
        }

    }
elif mode == 4:
    tileTypes = {

        "" : 
        {
            "name" : "",
            "png" : "",
            "ascii" : "○",

            "right" : [""],
            "rightWeights" : {},

            "left" : [""],
            "leftWeights" : {},

            "top" : [""],
            "topWeights" : {},

            "bottom" : [""],
            "bottomWeights" : {}
        },

        "floor" : 
        {
            "name" : "floor",
            "png" : "",
            "ascii" : " ",

            "right" : ["floor", "wall_right", "invert_bottomleft", "invert_topleft"],
            "rightWeights" : {"floor": 2},

            "left" : ["floor", "wall_left", "invert_bottomright", "invert_topright"],
            "leftWeights" : {"floor": 2},

            "top" : ["floor", "wall_top", "invert_bottomright", "invert_bottomleft"],
            "topWeights" : {"floor": 2},

            "bottom" : ["floor", "wall_bottom", "invert_topright", "invert_topleft"],
            "bottomWeights" : {"floor": 2}
        },

        "solid" : 
        {
            "name" : "solid",
            "png" : "",
            "ascii" : "█",

            "right" : ["solid", "wall_left", "corner_topleft", "corner_bottomleft"],
            "rightWeights" : {"solid": 0.5},

            "left" : ["solid", "wall_right", "corner_topright", "corner_bottomright"],
            "leftWeights" : {"solid": 0.5},

            "top" : ["solid", "wall_bottom", "corner_bottomright", "corner_bottomleft"],
            "topWeights" : {"solid": 0.5},

            "bottom" : ["solid", "wall_top", "corner_topright", "corner_topleft"],
            "bottomWeights" : {"solid": 0.5}
        },

        "wall_right" : 
        {
            "name" : "wall_right",
            "png" : "",
            "ascii" : "║",

            "right" : ["solid"],
            "rightWeights" : {},

            "left" : ["floor"],
            "leftWeights" : {},

            "top" : ["wall_right", "corner_topright", "invert_topleft"],
            "topWeights" : {"wall_right": 1.5},

            "bottom" : ["wall_right", "corner_bottomright", "invert_bottomleft"],
            "bottomWeights" : {"wall_right": 1.5}
        },

        "wall_left" : 
        {
            "name" : "wall_left",
            "png" : "",
            "ascii" : "║",

            "right" : ["floor"],
            "rightWeights" : {},

            "left" : ["solid"],
            "leftWeights" : {},

            "top" : ["wall_left", "corner_topleft", "invert_topright"],
            "topWeights" : {"wall_left": 1.5},

            "bottom" : ["wall_left", "corner_bottomleft", "invert_bottomright"],
            "bottomWeights" : {"wall_left": 1.5}
        },

        "wall_top" : 
        {
            "name" : "wall_top",
            "png" : "",
            "ascii" : "═",

            "right" : ["wall_top", "corner_topright", "invert_bottomright"],
            "rightWeights" : {"wall_top": 1.5},

            "left" : ["wall_top", "corner_topleft", "invert_bottomleft"],
            "leftWeights" : {"wall_top": 1.5},

            "top" : ["solid"],
            "topWeights" : {},

            "bottom" : ["floor"],
            "bottomWeights" : {}
        },

        "wall_bottom" : 
        {
            "name" : "wall_bottom",
            "png" : "",
            "ascii" : "═",

            "right" : ["wall_bottom", "corner_bottomright", "invert_topright"],
            "rightWeights" : {"wall_bottom": 1.5},

            "left" : ["wall_bottom", "corner_bottomleft", "invert_topleft"],
            "leftWeights" : {"wall_bottom": 1.5},

            "top" : ["floor"],
            "topWeights" : {},

            "bottom" : ["solid"],
            "bottomWeights" : {}
        },

        "corner_topright" : 
        {
            "name" : "corner_topright",
            "png" : "",
            "ascii" : "╗",

            "right" : ["solid"],
            "rightWeights" : {},

            "left" : ["wall_top", "invert_bottomleft"],
            "leftWeights" : {"wall_top": 1.5},

            "top" : ["solid"],
            "topWeights" : {},

            "bottom" : ["wall_right", "invert_bottomleft"],
            "bottomWeights" : {"wall_right": 1.5}
        },

        "corner_topleft" : 
        {
            "name" : "corner_topleft",
            "png" : "",
            "ascii" : "╔",

            "right" : ["wall_top", "invert_bottomright"],
            "rightWeights" : {"wall_top": 1.5},

            "left" : ["solid"],
            "leftWeights" : {},

            "top" : ["solid"],
            "topWeights" : {},

            "bottom" : ["wall_left", "invert_bottomright"],
            "bottomWeights" : {"wall_left": 1.5}
        },

        "corner_bottomright" : 
        {
            "name" : "corner_bottomright",
            "png" : "",
            "ascii" : "╝",

            "right" : ["solid"],
            "rightWeights" : {},

            "left" : ["wall_bottom", "invert_topleft"],
            "leftWeights" : {"wall_bottom": 1.5},

            "top" : ["wall_right", "invert_topleft"],
            "topWeights" : {"wall_right": 1.5},

            "bottom" : ["solid"],
            "bottomWeights" : {}
        },

        "corner_bottomleft" : 
        {
            "name" : "corner_bottomleft",
            "png" : "",
            "ascii" : "╚",

            "right" : ["wall_bottom", "invert_topright"],
            "rightWeights" : {"wall_bottom": 1.5},

            "left" : ["solid"],
            "leftWeights" : {},

            "top" : ["wall_left", "invert_topright"],
            "topWeights" : {"wall_left": 1.5},

            "bottom" : ["solid"],
            "bottomWeights" : {}
        },

        "invert_topright" : 
        {
            "name" : "invert_topright",
            "png" : "",
            "ascii" : "╗",

            "right" : ["floor"],
            "rightWeights" : {},

            "left" : ["wall_bottom", "corner_bottomleft"],
            "leftWeights" : {"wall_bottom": 1.5},

            "top" : ["floor"],
            "topWeights" : {},

            "bottom" : ["wall_left", "corner_bottomleft"],
            "bottomWeights" : {"wall_left": 1.5}
        },

        "invert_topleft" : 
        {
            "name" : "invert_topleft",
            "png" : "",
            "ascii" : "╔",

            "right" : ["wall_bottom", "corner_bottomright"],
            "rightWeights" : {"wall_bottom": 1.5},
            
            "left" : ["floor"],
            "leftWeights" : {},

            "top" : ["floor"],
            "topWeights" : {},

            "bottom" : ["wall_right", "corner_bottomright"],
            "bottomWeights" : {"wall_right": 1.5}
        },

        "invert_bottomright" : 
        {
            "name" : "invert_bottomright",
            "png" : "",
            "ascii" : "╝",

            "right" : ["floor"],
            "rightWeights" : {},

            "left" : ["wall_top", "corner_topleft"],
            "leftWeights" : {"wall_top": 1.5},

            "top" : ["wall_left", "corner_topleft"],
            "topWeights" : {"wall_left": 1.5},

            "bottom" : ["floor"],
            "bottomWeights" : {}
        },

        "invert_bottomleft" : 
        {
            "name" : "invert_bottomleft",
            "png" : "",
            "ascii" : "╚",

            "right" : ["wall_top", "corner_topright"],
            "rightWeights" : {"wall_top": 1.5},

            "left" : ["floor"],
            "leftWeights" : {},

            "top" : ["wall_right", "corner_topright"],
            "topWeights" : {"wall_right": 1.5},

            "bottom" : ["floor"],
            "bottomWeights" : {}
        }

    }

