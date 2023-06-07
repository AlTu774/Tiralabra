import pygame
from tile import Tile
from renderer import Renderer
from loop import Loop
from search import A_star, IDA_star

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
    loop.switch = 0

    while running:
        loop.events()
        if loop.end == True:
            for y in range(0, map_size):
                for x in range(0, map_size):
                    Tile.connect_nodes(map[y][x], (y,x), map)
            if loop.switch == 0:
                r = A_star(loop.start_node, loop.end_node, map, rnd, loop.ani, False)
            else:
                r = IDA_star(loop.start_node, loop.end_node, map, rnd, loop.ani, False)
            if r == "dead end":
                for row in map:
                    for tile in row:
                        if tile.color == (255,114,118):
                            tile.color = (230,230,230)
            if r == "restart":
                loop.clear_map()
            elif r == 1:
                loop.switch = 1
            elif r == 0:
                loop.switch = 0
            loop.end = False
        rnd.render_map()
        pygame.display.update()
    

if __name__ == "__main__":
    main()
