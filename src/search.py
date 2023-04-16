from math import sqrt
from collections import deque

def A_star(start,end,map):
    h = sqrt((end.y-start.y)**2+(end.x-start.y)**2)
    minlist = [(h,start)]
    g_list = []
    for i in range(len(map)):
        g_list.append(float('inf'))
    g_list[start.y][start.x] = 0

    while minlist != []:
        node = minlist.pop()[1]
        if node == end:
            return
        
        for neighbor in node.nodes:
            neighbor_g = g_list[node.y][node.x] + 1
            if neighbor_g < g_list[neighbor.y][neighbor.x]:
                g_list[neighbor.y][neighbor.x] = neighbor_g
                f = neighbor_g + sqrt((end.y-neighbor.y)**2+(end.x-neighbor.y)**2)
            if neighbor not in minlist:
                minlist.append((f,neighbor))
                minlist.sort()