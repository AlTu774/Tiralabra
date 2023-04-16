import pygame

class Tile():
    """Class that represents a single tile in a map.

    Attributes:
    x: tile's x coordinate in a map
    y: tile's y coordinate in a map
    color: the color of the tile
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.nodes = []
    
    def connect_nodes(c_node, node, map_size):
        """Connect's a node(tile) with it's surrounding nodes(tiles).
        
        Args:
        c_node: the node itself
        node: the node's coordinates in a map
        map_size: the size of the map
        """
        if node[1]-1 > 0:
            c_node.nodes.append((node[0],node[1]-1))
        if node[0]-1 > 0:
            c_node.nodes.append((node[0]-1,node[1]))
        if node[1]+1 < (map_size-1):
            c_node.nodes.append((node[0],node[1]+1))
        if node[0]+1 < (map_size-1):
            c_node.nodes.append((node[0]+1,node[1]))
