from math import sqrt

class Priority_queue():
    def __init__(self):
        self.queue = []
    
    def add_node(self, node):
        if self.queue == []:
            self.queue.append(node)
        else:
            holder = []
            while self.queue != []:
                if self.queue[-1][0] > node[0]:
                    self.queue.append(node)
                    break
                elif self.queue[-1][0] <= node[0]:
                    holder.append(self.take_node())
            if self.queue == []:
                self.queue.append(node)
            for n in reversed(holder):
                self.queue.append(n)
    
    def take_node(self):
        return self.queue.pop()

def A_star(start, end, map, rnd):
    visited = [start]
    h = sqrt((end.y-start.y)**2+(end.x-start.y)**2)
    list = Priority_queue()
    list.add_node((h,(start.y,start.x)))
    g_list = [[float('inf') for x in range(len(map))] for x in range(len(map))]
    g_list[start.y][start.x] = 0

    while list.queue != []:
        node = list.take_node()[1]
        node = map[node[1]][node[0]]
        if node == end:
            list.queue == []
            break
        
        for neighbor in node.nodes:
            neighbor = map[neighbor[0]][neighbor[1]]
            neighbor_g = g_list[node.y][node.x] + 1
            f = neighbor_g + sqrt((end.y-neighbor.y)**2+(end.x-neighbor.x)**2)

            if neighbor_g < g_list[neighbor.y][neighbor.x]:
                g_list[neighbor.y][neighbor.x] = neighbor_g
                if neighbor not in list.queue:
                    list.add_node((f,(neighbor.y,neighbor.x)))
                    if neighbor.color != (200,200,200):
                        visited.append(neighbor)
            rnd.vizualize_search(visited)
    
