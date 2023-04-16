import pygame
from search import A_star

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
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                y = pos[0]//self.tile_size
                x = pos[1]//self.tile_size
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
                y = pos[0]//self.tile_size
                x = pos[1]//self.tile_size
                if y >= self.len or x >= self.len:
                    continue
                self.map[y][x].color = (200,200,200)
            
