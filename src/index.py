import pygame
from tile import Tile
from renderer import Renderer
from loop import Loop

def main():
    display_size = 1000
    display = pygame.display.set_mode((1000,1000))
    
    pygame.init()

    white = (255,255,255)
    gray = (220,220,220)

    map_size = 100
    map = []
    tile_size = display_size//map_size
    print(tile_size)

    for i in range(map_size):
        map.append([])
        for j in range(map_size):
            tile1 = Tile(i,j,white)
            map[i].append(tile1)
    
    for y in range(0, map_size):
        for x in range(0, map_size):
            Tile.connect_nodes(map[y][x], (y,x), map_size)
    
    rnd = Renderer(display, display_size, map, tile_size)
    rnd.render_map()
    pygame.display.update()

    running = True
    loop = Loop(map, tile_size)

    while running:
        loop.events()
        rnd.render_map()
        pygame.display.update()
    

if __name__ == "__main__":
    main()
