import unittest
import pygame
from tile import Tile
from search import A_star

class Test_Search(unittest.TestCase):
    def setUp(self):
        self.map = []
        map_size = 50
        self.rnd = None
        pygame.init()

        for i in range(map_size):
            self.map.append([])
            for j in range(map_size):
                tile1 = Tile(i,j,(255,255,255))
                self.map[i].append(tile1)
        
        for y in range(0, map_size):
            for x in range(0, map_size):
                Tile.connect_nodes(self.map[y][x], (y,x), self.map)
    
    def test_astar(self):
        result = A_star((self.map[20][30]),(self.map[25][35]), self.map, self.rnd, False, True)
        m = self.map
        correct = [(20,30),(21,31),(22,32),(23,33),(24,34),(25,35)]

        self.assertEqual(result, correct)
