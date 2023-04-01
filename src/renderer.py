import pygame

class Renderer():
    def __init__(self, display, display_size, map, tile_size):
        self.display = display
        self.display_size = display_size
        self.map = map
        self.map_size = len(self.map)
        self.tile_size = tile_size
    
    def render_map(self):
        tile_size = self.display_size//self.map_size
        for y in range(0, self.map_size):
            for x in range(0, self.map_size):
                pygame.draw.rect(self.display, self.map[y][x].color, (y*tile_size, x*tile_size, tile_size, tile_size))
