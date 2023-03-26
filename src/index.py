import pygame
from tile import Tile
from renderer import Renderer

def main():
    display_size = 700
    display = pygame.display.set_mode((700,700))
    
    pygame.init()

    white = (255,255,255)
    gray = (220,220,220)

    map_size = 50
    map = []

    for i in range(map_size):
        map.append([])
        for j in range(map_size):
            tile1 = Tile(i,j,white)
            map[i].append(tile1)
    
    rnd = Renderer(display, display_size, map)
    rnd.render_map()
    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    

if __name__ == "__main__":
    main()
