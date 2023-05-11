import pygame

class Renderer():
    """Class that renders visualisation of search algoriths on screen.

    Attributes:
    display: the display
    display_size: given size of the display
    map: the map which will be rendered
    tile_size: how many pixels a single tile is
    """
    def __init__(self, display, display_size, map, tile_size):
        self.display = display
        self.display_size = display_size
        self.map = map
        self.map_size = len(self.map)
        self.tile_size = tile_size
        self.path = 0
    
    def render_map(self):
        tile_size = self.display_size//self.map_size
        for y in range(0, self.map_size):
            for x in range(0, self.map_size):
                pygame.draw.rect(self.display, self.map[y][x].color, (x*tile_size, y*tile_size, tile_size, tile_size))
        pygame.display.update()
    
    def visualize_search(self, visited):
        for node in visited:
            node.color = (255,114,118)
        self.render_map()
        pygame.display.update()
    
    def visualize_depth(self, path):
        c = path.copy()
        if self.path == 0:
            self.path = c
        else:
            for node in self.path:
                node.color = (255,255,255)
        for node in path:
            node.color = (255,114,118)
        
        self.path = c
        self.render_map()
        pygame.display.update()
    

        
