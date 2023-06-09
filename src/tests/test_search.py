import unittest
import pygame
import random
from tile import Tile
from search import A_star
from search import IDA_star

class Test_Search(unittest.TestCase):
    def setUp(self):
        self.map = []
        self.map_size = 20
        self.rnd = None
        pygame.init()

        for i in range(self.map_size):
            self.map.append([])
            for j in range(self.map_size):
                tile1 = Tile(i,j,(255,255,255))
                self.map[i].append(tile1)
        
    
    def test_astar(self):
        for y in range(0, self.map_size):
            for x in range(0, self.map_size):
                Tile.connect_nodes(self.map[y][x], (y,x), self.map)
        
        result = A_star((self.map[5][10]),(self.map[10][15]), self.map, self.rnd, False, True)
        m = self.map
        result = result[0]
        correct = [(5,10),(6,11),(7,12),(8,13),(9,14),(10,15)]

        self.assertEqual(result, correct)
    
    def test_astar_map(self):
        t_map = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"," ","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"," ","#"],
                 ["#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#"," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]
        
        t_mapAD =[["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","1","1","1","1","1","1","1","1","1","1","1","1"," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","1","#","#","#","#","#","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," ","1"," "," "," "," "," ","#"],
                 ["#","1","1","1","1","1","1","1","1","1","1","1","1"," "," "," "," "," "," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"," ","#"," ","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","1","#"," ","#"],
                 ["#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#"," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]
        
        for i in range(self.map_size):
            for j in range(self.map_size):
                if t_map[i][j] == "#":
                    self.map[i][j].color = (200,200,200)
        
        for y in range(0, self.map_size):
            for x in range(0, self.map_size):
                Tile.connect_nodes(self.map[y][x], (y,x), self.map)
        
        result = A_star((self.map[1][1]),(self.map[11][16]), self.map, self.rnd, False, True)
        result1 = result[0]
        for r in result1:
            t_map[r[0]][r[1]] = "1"
        AD_l = result[1]
        AD_l = round(AD_l, 5)
        
        self.assertEqual(t_map, t_mapAD)
        
        for r in result1:
            t_map[r[0]][r[1]] = " "

        result = A_star((self.map[11][16]),(self.map[1][1]), self.map, self.rnd, False, True)
        result1 = result[0]
        for r in result1:
            t_map[r[0]][r[1]] = "1"
        DA_l = result[1]
        DA_l = round(DA_l, 5)

        self.assertEqual(AD_l, DA_l)

        for r in result1:
            t_map[r[0]][r[1]] = " "

        t_mapAC =[["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","1","1","1","1","1","1","1","1","1","1","1","1"," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","1","#","#","#","#","#","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," ","1"," "," "," "," "," ","#"],
                 ["#","1","1","1","1","1","1","1","1","1","1","1","1"," "," "," "," "," "," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1","#","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","#"],
                 ["#","1","#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#","1","1","1","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]
        
        result = A_star((self.map[1][1]),(self.map[13][18]), self.map, self.rnd, False, True)
        result1 = result[0]
        for r in result1:
            t_map[r[0]][r[1]] = "1"
        AC_l = result[1]
        AC_l = round(AC_l, 5)
        
        self.assertEqual(t_map, t_mapAC)

        for r in result1:
            t_map[r[0]][r[1]] = " "
        
        result = A_star((self.map[13][18]),(self.map[1][1]), self.map, self.rnd, False, True)
        result1 = result[0]
        for r in result1:
            t_map[r[0]][r[1]] = "1"
        CA_l = result[1]
        CA_l = round(CA_l, 5)

        self.assertEqual(AC_l, CA_l)

        for r in result1:
            t_map[r[0]][r[1]] = " "
        
        t_mapAB =[["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#"," ","1","1","1","1","1","1","1","1","1","1","1","1"," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","1","#","#","#","#","#","#"],
                 ["#"," "," "," "," "," "," "," "," "," "," "," "," ","1"," "," "," "," "," ","#"],
                 ["#","1","1","1","1","1","1","1","1","1","1","1","1"," "," "," "," "," "," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"," ","#"],
                 ["#","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"," ","#"],
                 ["#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","1","#","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","#"],
                 ["#","1","#","1","#","#","#","#","#","#","#","#","#","#","#","#","#","#","1","#"],
                 ["#","1","1","1","#"," ","1","1","1","1","1","1","1","1","1","1","1","1","1","#"],
                 ["#"," "," "," ","#","1"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]
        
        result = A_star((self.map[1][1]),(self.map[16][5]), self.map, self.rnd, False, True)
        result1 = result[0]
        for r in result1:
            t_map[r[0]][r[1]] = "1"
        AB_l = result[1]
        AB_l = round(AB_l, 5)

        self.assertEqual(t_map, t_mapAB)

        for r in result1:
            t_map[r[0]][r[1]] = " "
        
        result = A_star((self.map[16][5]),(self.map[1][1]), self.map, self.rnd, False, True)
        result1 = result[0]
        for r in result1:
            t_map[r[0]][r[1]] = "1"
        BA_l = result[1]
        BA_l = round(BA_l, 5)
 
        self.assertEqual(AB_l, BA_l)

        for r in result1:
            t_map[r[0]][r[1]] = " "
    


    def test_IDA(self):
        map = []
        map_size = 7
        rnd = None
        pygame.init()

        for i in range(map_size):
            map.append([])
            for j in range(map_size):
                tile1 = Tile(i,j,(255,255,255))
                map[i].append(tile1)
        
        t_map = [[" "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "],
                 [" "," "," ","#"," "," "," "],
                 [" "," ","#"," "," "," "," "],
                 ["#","#"," "," "," ","#","#"],
                 [" "," "," "," "," "," "," "],
                 ["#","#"," "," "," "," "," "]]
        
        for i in range(map_size):
            for j in range(map_size):
                if t_map[i][j] == "#":
                    map[i][j].color = (200,200,200)
        
        for y in range(0, map_size):
            for x in range(0, map_size):
                Tile.connect_nodes(map[y][x], (y,x), map)
        
        start = random_point(t_map,map_size)
        end = random_point(t_map,map_size)

        r1 = A_star(map[start[0]][start[1]], map[end[0]][end[1]], map, rnd, False, True)
        r2 = IDA_star(map[start[0]][start[1]], map[end[0]][end[1]] , map, rnd, False, True)
        r1 = r1[1]
        r2 = r2[1]

        self.assertEqual(r1, r2)

def random_point(t_map, map_size):
    r = (random.randint(0,map_size-1),random.randint(0,map_size-1))
    if t_map[r[0]][r[1]] != "#":
        pass
    else:
        while t_map[r[0]][r[1]] == "#":
            r = (random.randint(0,map_size-1),random.randint(0,map_size-1))
    return r

        

        
