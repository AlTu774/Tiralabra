import unittest
import pygame
from tile import Tile
from renderer import Renderer
from search import A_star


class Test_Search(unittest.TestCase):
    def setUp(self):
        self.map = []
        map_size = 50
        display_size = 1000
        display = pygame.display.set_mode((500,500))
        tile_size = display_size//map_size
        self.rnd = Renderer(display, display_size, self.map, tile_size)
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
        result = A_star((self.map[20][30]),(self.map[25][35]),self.map, self.rnd)
        m = self.map
        correct = [m[20][30],m[21][31],m[22][32],m[23][33],m[24][34],m[22][32]]

        self.assertEqual(result, correct)

if __name__ == '__main__':
    unittest.main()