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

def A_star(start, end, map, rnd, ani, test):
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
            path = shortest_path(path_map, start, node, map, rnd)
            return path
        
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
            if ani:
                rnd.visualize_search(visited)

            if not test:    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if pygame.mouse.get_pressed()[2]:
                        return "restart"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            return 1


def IDA_star(start, end, map, rnd, ani):
    #print(end.y, end.x)
    diff_d = min(abs(end.x - start.x),abs(end.y - start.y))*sqrt(2)
    diff_h = abs(abs(end.x - start.x)-abs(end.y - start.y))
    h = round(diff_d + diff_h, 3)
    #h = abs(end.y-start.y)+abs(end.x-start.x)
    limit = h
    path = [start]

    while True:
        res = depth_search(path, map, 0, end, limit, rnd, ani)
        if res == "end":
            rnd.visualize_depth(path)
            break
        if res == "restart":
            return "restart"
        if res == float('inf'):
            break
        limit = res


def depth_search(path, map, g, end_node, limit, rnd, ani):
    if ani:
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
    #print(abs(end_node.x - node.x),abs(end_node.y - node.y), "diagonal lenght")
    diff_d = min(abs(end_node.x - node.x),abs(end_node.y - node.y))*sqrt(2)
    diff_h = abs(abs(end_node.x - node.x)-abs(end_node.y - node.y))
    h = diff_d + diff_h
    f = round(g + h, 3)
    #f = g + abs(end_node.y-node.y)+abs(end_node.x-node.x)
    #print("diff_diag", diff_d,"diff_hori", diff_h, "G",g, "F", f)
    #print("limit",limit, node.y, node.x)
    if f > limit:
        #print("TOO BIG")
        return f
    elif node == end_node:
        return "end"
    min_val = float('inf')

    neighbors = prioritize_neigbors(node, end_node, g, map)

    for neighbor in neighbors:
        if neighbor not in path:
            path.append(neighbor)
            n = (neighbor.y, neighbor.x)
            if n == (node.y+1, node.x+1) or n == (node.y-1, node.x-1) or n == (node.y-1, node.x+1) or n == (node.y+1, node.x-1):
                neighbor_g = g + sqrt(2)
            else:
                neighbor_g = g + 1
            res = depth_search(path, map, neighbor_g, end_node, limit, rnd, ani)
            if res == "end":
                return "end"
            if res == "restart":
                return "restart"
            elif res < min_val:
                min_val = res
            path.pop()
    return min_val


def shortest_path(path_map, start, end, map, rnd):
    node = (end.y, end.x)
    path = [node]
    while node != (start.y, start.x):
        node = path_map[node[0]][node[1]]
        map[node[0]][node[1]].color = (173,216,230)
        path.append(node)
        if rnd != None:
            print("JIO")
            rnd.render_map()
    path.reverse()
    return path
        

def prioritize_neigbors(node, end_node, g, map):
    neighbors = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if node.x+i < 0 or node.x+i >= len(map):
                continue
            if node.y+j < 0 or node.y+j >= len(map):
                continue
            
            diff_d = min(abs(end_node.x - (node.x+i)),abs(end_node.y - (node.y+j)))*sqrt(2)
            diff_h = abs(abs(end_node.x - (node.x+i))-abs(end_node.y - (node.y+j)))
            neighbor_h = diff_d + diff_h
            #neighbor_h =sqrt((end_node.y-node.y)**2+(end_node.x-node.x)**2)
            if (node.y+j, node.x+i) in node.nodes:
                neighbors.append((neighbor_h, node.y+j,node.x+i))
    
    neighbors = sorted(neighbors)
    neighbors_s = []
    for n in neighbors:
        #print(n[0], n[1], n[2])
        neighbors_s.append(map[n[1]][n[2]])
    return neighbors_s
