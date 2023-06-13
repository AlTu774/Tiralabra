from math import sqrt
from heapq import heappush, heappop
import pygame

class Priority_queue():
    """Class for using priority queue.
    Attributes:
    queue: stack which sorts to lowest value to be on top of the stack
    
    add_node(self, node): function that adds a new node to the stack
    take_node(self, node): function that returns the lowest value and removes it from the stack
    """
    def __init__(self):
        self.queue = []

    def add_node(self,node):
        heappush(self.queue, node)
    
    def take_node(self):
        return heappop(self.queue)

def A_star(start, end, map, rnd, ani, test):
    """A* function.
    Args:
    start: starting point on map, tile
    end: goal point on map, tile
    map: matrix of map that contains tiles
    rnd: renderer used for visualization
    ani: if the search is animated or not, bool
    test: if the search is used for testing or not, bool

    Returns:
    "dead end" if path was not found
    "restart" if the search will be stopped
    (path, lenght) tuple if the shortest path is found
    1, if there is a switch to IDA* search
    """
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
            return (path, g_list[end.y][end.x])
        
        for neighbor in node.nodes:
            neighbor = map[neighbor[0]][neighbor[1]]
            if (neighbor.y, neighbor.x) == (node.y+1, node.x+1) or (neighbor.y, neighbor.x) == (node.y-1, node.x-1) or (neighbor.y, neighbor.x) == (node.y-1, node.x+1) or (neighbor.y, neighbor.x) == (node.y+1, node.x-1):
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
    return "dead end"


def IDA_star(start, end, map, rnd, ani, test):
    """IDA* function.
    Args:
    start: starting point on map, tile
    end: goal point on map, tile
    map: matrix of map that contains tiles
    rnd: renderer used for visualization
    ani: if the search is animated or not, bool
    test: if the search is used for testing or not, bool

    Returns:
    "dead end" if path was not found
    "restart" if the search will be stopped
    ("end", lenght) tuple if the shortest path is found
    """
    diff_d = min(abs(end.x - start.x),abs(end.y - start.y))*sqrt(2)
    diff_h = abs(abs(end.x - start.x)-abs(end.y - start.y))
    h = round(diff_d + diff_h, 3)
    limit = h
    path = [start]

    while True:
        res = depth_search(path, map, 0, end, limit, rnd, ani, test)
        if res[0] == "end":
            if not test:
                rnd.visualize_depth(path)
            return res
        if res[0] == "restart":
            return "restart"
        if res[0] == float('inf'):
            return "dead end"
        limit = res[0]


def depth_search(path, map, g, end_node, limit, rnd, ani, test):
    """depth search for IDA* algorithm.
    Args:
    path: list containing the current path algorithm is on
    map: matrix of map that contains tiles
    g: g value, lenght of path from starting node to current node, int
    end_node: goal point on map, tile
    limit: limit for f value, initially the shortest path from start to end if there are no walls, int
    rnd: renderer used for visualization
    ani: if the search is animated or not, bool
    test: if the search is used for testing or not, bool
    
    Returns:
    "restart" if the search will be stopped
    ("end", lenght) tuple if the shortest path is found
    1, if there is a switch to A* search
    """
    if ani:
        rnd.visualize_depth(path)
    if not test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.mouse.get_pressed()[2]:
                return "restart"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return 1
    node = path[-1]
    diff_d = min(abs(end_node.x - node.x),abs(end_node.y - node.y))*sqrt(2)
    diff_h = abs(abs(end_node.x - node.x)-abs(end_node.y - node.y))
    h = diff_d + diff_h
    f = round(g + h, 3)
    if f > limit:
        return (f, g)
    elif node == end_node:
        return ("end", g)
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
            res = depth_search(path, map, neighbor_g, end_node, limit, rnd, ani, test)
            if res[0] == "end":
                return ("end", res[1])
            if res[0] == "restart":
                return "restart"
            elif res[0] < min_val:
                min_val = res[0]
            path.pop()
    return (min_val,0)


def shortest_path(path_map, start, end, map, rnd):
    """Function that returns the shortest path on the map by tracing back fron end point.
    
    Args:
    path_map: matrix the size of the map, index points to previous node from current node
    start: starting tile
    end: goal tile
    map: matrix of map that contains tiles
    renderer used for visualization
    """
    node = (end.y, end.x)
    path = [node]
    while node != (start.y, start.x):
        node = path_map[node[0]][node[1]]
        map[node[0]][node[1]].color = (173,216,230)
        path.append(node)
        if rnd != None:
            rnd.render_map()
    path.reverse()
    return path
        

def prioritize_neigbors(node, end_node, map):
    """Function that sorts the neighboring nodes in the order of best heurestic first.
    
    Args:
    node: the node whose neighbors are sorted, tile
    end_node: goal node, tile
    map: matrix of map that contains tiles
    
    Return:
    A list with the sorted neighboring nodes"""
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
            if (node.y+j, node.x+i) in node.nodes:
                neighbors.append((neighbor_h, node.y+j,node.x+i))
    
    neighbors = sorted(neighbors)
    neighbors_s = []
    for n in neighbors:
        neighbors_s.append(map[n[1]][n[2]])
    return neighbors_s
