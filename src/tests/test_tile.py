import unittest
from tile import Tile

class Test_Tile(unittest.TestCase):
    
    def test_connect_node(self):
        map_size = 50
        node = Tile(0,0,(255,255,255))
        Tile.connect_nodes(node,(0,0),map_size)
        self.assertEqual(sorted([(0,1),(1,0)]), sorted(node.nodes))

        node = Tile(49,0,(255,255,255))
        Tile.connect_nodes(node,(0,49), map_size)
        self.assertEqual(sorted([(0,48),(1,49)]), sorted(node.nodes))

        node = Tile(0,49,(255,255,255))
        Tile.connect_nodes(node, (49,0), map_size)
        self.assertEqual(sorted(node.nodes), sorted([(48,0),(49,1)]))

if __name__ == '__main__':
    unittest.main()