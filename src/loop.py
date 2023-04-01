import pygame

class Loop():
    def __init__(self, map, tile_size):
        self.map = map
        self.tile_size = tile_size
        self.len = len(map)
        self.start = False
        self.end = False
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
                    continue
                if not self.end:
                    self.map[y][x].color = (255,160,0)
                    self.end = True
                    continue

            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                y = pos[0]//self.tile_size
                x = pos[1]//self.tile_size
                if y >= self.len or x >= self.len:
                    continue
                self.map[y][x].color = (200,200,200)
            
