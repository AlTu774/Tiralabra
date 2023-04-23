import unittest
from tile import Tile

class Test_Tile(unittest.TestCase):
    
    def test_connect_node(self):
        map_size = 50
        map = []
        for i in range(map_size):
            map.append([])
            for j in range(map_size):
                tile1 = Tile(i,j,(255,255,255))
                map[i].append(tile1)

        node = map[0][0]
        Tile.connect_nodes(node,(0,0),map)
        self.assertEqual(sorted([(0,1),(1,0),(1,1)]), sorted(node.nodes))

        node = map[0][49]
        Tile.connect_nodes(node,(0,49), map_size)
        self.assertEqual(sorted([(0,48),(1,49),(1,48)]), sorted(node.nodes))

        node = map[49][0]
        Tile.connect_nodes(node, (49,0), map_size)
        self.assertEqual(sorted(node.nodes), sorted([(48,0),(49,1),(48,1)]))

if __name__ == '__main__':
    unittest.main()