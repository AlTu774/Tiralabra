from math import sqrt
from heapq import heappush, heappop
import pygame

class Priority_queue():
    def __init__(self):
        self.queue = []

    def add_node(self,node):
        heappush(self.queue, node)
    
    def take_node(self):
        return heappop(self.queue)

def A_star(start, end, map, rnd):
    visited = [start]
    h = sqrt((end.y-start.y)**2+(end.x-start.x)**2)
    prev = 0
    list = Priority_queue()
    list.add_node([h,(start.y,start.x), prev])
    g_list = [[float('inf') for x in range(len(map))] for x in range(len(map))]
    g_list[start.y][start.x] = 0

    path_map = []
    for y in range(0,len(map)):
        m = []
        for x in range(0,len(map)):
            m.append(None)
        path_map.append(m)

    while list.queue != []:
        node = list.take_node()[1]
        node = map[node[0]][node[1]]
        
        if node == end:
            shortest_path(path_map, start, node, map, rnd)
            return path_map
        
        for neighbor in node.nodes:
            neighbor = map[neighbor[0]][neighbor[1]]
            if (neighbor.y, neighbor.x) == (node.y+1, node.x+1) or (node.y-1, node.y-1) or (node.y-1, node.x+1) or (node.y+1, node.x-1):
                neighbor_g = g_list[node.y][node.x] + sqrt(2)
            
            else:
                neighbor_g = g_list[node.y][node.x] + 1
            f = neighbor_g + sqrt((end.y-neighbor.y)**2+(end.x-neighbor.x)**2)

            if neighbor_g < g_list[neighbor.y][neighbor.x]:
                path_map[neighbor.y][neighbor.x] = (node.y, node.x)
                g_list[neighbor.y][neighbor.x] = neighbor_g
                if neighbor not in list.queue:
                    list.add_node([f,(neighbor.y,neighbor.x)])
                    prev = (neighbor.y,neighbor.x)
                    if neighbor.color != (200,200,200):
                        visited.append(neighbor)

            rnd.visualize_search(visited)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if pygame.mouse.get_pressed()[2]:
                    return "restart"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        return 1

def IDA_star(start, end, map, rnd):
    g_list = [[float('inf') for x in range(len(map))] for x in range(len(map))]
    h = sqrt((end.y-start.y)**2+(end.x-start.x)**2)
    #h = abs(end.y-start.y)+abs(end.x-start.x)
    limit = h
    path = [start]

    while True:
        res = depth_search(path, map, 0, end, limit, rnd)
        if res == "end":
            #shortest_path(path, start, end, map, rnd)   
            break
        if res == "restart":
            return "restart"
        if res == float('inf'):
            break
        limit = res


def depth_search(path, map, g, end_node, limit, rnd):
    rnd.visualize_depth(path)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[2]:
            return "restart"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                return 1
    node = path[-1]
    f = g + sqrt((end_node.y-node.y)**2+(end_node.x-node.x)**2)
    #f = g + abs(end_node.y-node.y)+abs(end_node.x-node.x)
    if f > limit:
        return f
    elif node == end_node:
        return "end"
    min_val = float('inf')

    neighbors = prioritize_neigbors(node, end_node, g, map)

    for neighbor in neighbors:
        if neighbor not in path:
            path.append(neighbor)
            if (neighbor.y, neighbor.x) == ((node.y+1, node.x+1) or (node.y-1, node.y-1) or (node.y-1, node.x+1) or (node.y+1, node.x-1)):
                neighbor_g = g + sqrt(2)
            else:
                neighbor_g = g + 1
            res = depth_search(path, map, neighbor_g, end_node, limit, rnd)
            if res == "end":
                return "end"
            if res == "restart":
                return "restart"
            elif res < min_val:
                min_val = res
            path.pop()
    return min_val


def JPS():
    pass
    

def shortest_path(path_map, start, end, map, rnd):
    node = (end.y, end.x)
    while node != (start.y, start.x):
        node = path_map[node[0]][node[1]]
        map[node[0]][node[1]].color = (173,216,230)
        rnd.render_map()
    return path_map
        

def visualize_queue(queue, map, rnd):
    for node in queue:
        c = node[1]
        map[c[1]][c[0]].color = (240,240,255)
        rnd.render_map()

def prioritize_neigbors(node, end_node, g, map):
    neighbors = []
    if end_node.y - node.y < 0 and end_node.x - node.x < 0:
        if (node.y-1,node.x-1) in node.nodes:
            neighbors.append(map[node.y-1][node.x-1])

    elif end_node.y - node.y > 0 and end_node.x - node.x > 0:
        if (node.y+1,node.x+1) in node.nodes:
            neighbors.append(map[node.y+1][node.x+1])

    elif end_node.y - node.y < 0 and end_node.x - node.x > 0:
        if (node.y+1,node.x-1) in node.nodes:
            neighbors.append(map[node.y+1][node.x-1])
    
    elif end_node.y - node.y > 0 and end_node.x - node.x < 0:
        if (node.y+1,node.x+1) in node.nodes:
            neighbors.append(map[node.y+1][node.x+1])
    
    remaining = []
    for n_node in node.nodes:
        neighbor = map[n_node[0]][n_node[1]]
        if neighbor not in neighbors:
            neighbor_h = g + sqrt((end_node.y-neighbor.y)**2+(end_node.x-neighbor.x)**2)
            remaining.append((neighbor_h, neighbor))

    remaining.sort(key=lambda a: a[0])
    for n in remaining:
        neighbors.append(n[1])
    return neighbors

def prioritize_neigbors1(node, end_node, g, map):
    neighbors = []
    if end_node.y - node.y < 0:
        if (node.y-1,node.x) in node.nodes:
            neighbors.append(map[node.y-1][node.x])
    elif end_node.y - node.y > 0:
        if (node.y+1,node.x) in node.nodes:
            neighbors.append(map[node.y+1][node.x])
    
    if end_node.x - node.x < 0:
        if (node.y,node.x-1) in node.nodes:
            neighbors.append(map[node.y][node.x-1])
    elif end_node.x - node.x > 0:
        if (node.y,node.x+1) in node.nodes:
            neighbors.append(map[node.y][node.x+1])
    
    remaining = []
    for n_node in node.nodes:
        neighbor = map[n_node[0]][n_node[1]]
        if neighbor not in neighbors:
            neighbor_h = abs(end_node.y-neighbor.y)+abs(end_node.x-neighbor.x)
            remaining.append((neighbor_h, neighbor))

    remaining.sort(key=lambda a: a[0])
    for n in remaining:
        neighbors.append(n[1])
    return neighbors