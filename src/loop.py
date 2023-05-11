import pygame
from search import A_star
from tile import Tile

class Loop():
    def __init__(self, map, tile_size):
        self.map = map
        self.tile_size = tile_size
        self.len = len(map)
        self.start = False
        self.start_node = None
        self.end = False
        self.end_node = None
        self.down = False
        self.switch = 0
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if self.switch == 0:
                        self.switch = 1
                    else:
                        self.switch = 0
                if event.key == pygame.K_a:
                    self.clear_map()
            
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                x = pos[0]//self.tile_size
                y = pos[1]//self.tile_size
                if y >= self.len or x >= self.len:
                    continue
                if not self.start:
                    self.map[y][x].color = (240,0,255)
                    self.start = True
                    self.start_node = self.map[y][x]
                    continue
                if not self.end:
                    self.map[y][x].color = (255,160,0)
                    self.end = True
                    self.end_node = self.map[y][x] 
                    continue

            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x = pos[0]//self.tile_size
                y = pos[1]//self.tile_size
                if y >= self.len or x >= self.len:
                    continue
                self.map[y][x].color = (200,200,200)
    
    def clear_map(self):
        map_size = len(self.map)
        for i in range(map_size):
            for j in range(map_size):
                self.map[i][j].color = (255,255,255)
        
        for line in self.map:
            for node in line:
                node.nodes = []

        self.start = False
        self.end = False
        self.start_node = None
        self.end_node = None

