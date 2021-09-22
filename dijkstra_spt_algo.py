# Dijkstra's Shortest Pathfinding Algorithm
import sys

class Graph():
    def __init__(self, vertices):
        # initialises array with nodes
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def solution_out(self, distance):
        print(f'Vertex \t Distance from Root')
        for node in range(self.V):
            print(f'{node} \t {distance[node]}')

    def minimum_distance(self, distance, spt):
        # finds min distance value from vertices not in shortest path tree
        min = sys.maxsize

        # searches for nearest vertex not in spt
        for u in range(self.V):
            if distance[u] < min and not spt[u]:
                min = distance[u]
                min_index = u
        return min_index
        
    def dijkstra(self, src):
        # implements Dijkstra's single source sp algo
        # for graph represented using adjacency matrices
        distance = [sys.maxsize] * self.V
        distance[src] = 0
        spt = [False] * self.V

        for i in range(self.V):
            # pick min distance vertex not yet processed
            x = self.minimum_distance(distance, spt)

            # add minimum distance vertex to spt
            spt[x] = True

            # update distance value of adjacent vertices if the
            # current distance is greater than the new distance
            for j in range(self.V):
                if self.graph[x][j] > 0 and not spt[j] and \
                distance[j] > distance[x] + self.graph[x][j]:
                    distance[j] = distance[x] + self.graph[x][j]

        self.solution_out(distance)

# set up and running
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
                
