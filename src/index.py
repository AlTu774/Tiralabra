import pygame
from tile import Tile
from renderer import Renderer
from loop import Loop
from search import A_star

def main():
    display_size = 1000
    display = pygame.display.set_mode((1000,1000))
    
    pygame.init()

    white = (255,255,255)

    map_size = 100
    map = []
    tile_size = display_size//map_size

    for i in range(map_size):
        map.append([])
        for j in range(map_size):
            tile1 = Tile(i,j,white)
            map[i].append(tile1)
    
    rnd = Renderer(display, display_size, map, tile_size)
    rnd.render_map()
    pygame.display.update()

    running = True
    loop = Loop(map, tile_size)

    while running:
        loop.events()
        if loop.end == True:
            for y in range(0, map_size):
                for x in range(0, map_size):
                    Tile.connect_nodes(map[y][x], (y,x), map)
            A_star(loop.start_node, loop.end_node, map, rnd)
            loop.end = False
        rnd.render_map()
        pygame.display.update()
    

if __name__ == "__main__":
    main()
