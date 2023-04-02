import pygame

class Tile():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.nodes = []
    
    def connect_nodes(c_node, node, map_size):
        if node[1]-1 > 0:
            c_node.nodes.append((node[0],node[1]-1))
        if node[0]-1 > 0:
            c_node.nodes.append((node[0]-1,node[1]))
        if node[1]+1 < map_size:
            c_node.nodes.append((node[0],node[1]+1))
        if node[0]+1 < map_size:
            c_node.nodes.append((node[0],node[1]+1))
