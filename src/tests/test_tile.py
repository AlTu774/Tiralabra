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
        Tile.connect_nodes(node,(0,49), map)
        self.assertEqual(sorted([(0,48),(1,49),(1,48)]), sorted(node.nodes))

        node = map[49][0]
        Tile.connect_nodes(node, (49,0), map)
        self.assertEqual(sorted(node.nodes), sorted([(48,0),(49,1),(48,1)]))

        node = map[15][16]
        Tile.connect_nodes(node, (15,16), map)
        self.assertEqual(sorted(node.nodes), sorted([(14,16),(14,17),(15,17),(16,17),(16,16),(16,15),(15,15),(14,15)]))

if __name__ == '__main__':
    unittest.main()