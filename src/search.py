from math import sqrt

def A_star(start, end, map, rnd):
    visited = [start]
    h = sqrt((end.y-start.y)**2+(end.x-start.y)**2)
    minlist = [(h,(start.y,start.x))]
    g_list = [[float('inf') for x in range(len(map))] for x in range(len(map))]
    g_list[start.y][start.x] = 0

    while minlist != []:
        node = minlist.pop()[1]
        node = map[node[1]][node[0]]
        if node == end:
            minlist == []
            break
        
        for neighbor in node.nodes:
            neighbor = map[neighbor[0]][neighbor[1]]
            neighbor_g = g_list[node.y][node.x] + 1
            f = neighbor_g + sqrt((end.y-neighbor.y)**2+(end.x-neighbor.y)**2)
            if neighbor_g < g_list[neighbor.y][neighbor.x]:
                g_list[neighbor.y][neighbor.x] = neighbor_g
                if neighbor not in minlist:
                    minlist.append((f,(neighbor.y,neighbor.x)))
                    minlist.sort()
                    visited.append(neighbor)
            rnd.vizualize_search(visited)