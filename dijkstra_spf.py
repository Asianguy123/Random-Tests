# Dijkstra's Shortest Pathfinding Algorithm

class Graph:
     
    def __init__(self, graph):
        self.graph = graph

    def display_shortest_path(self, visited, source, destination):
        self.current_node = destination
        self.path = destination
        while self.current_node != source:
            self.previous_node = visited[self.current_node][1]
            self.path = self.previous_node + self.path  
            self.current_node = visited[self.current_node][1]
        print(f'Shortest path from {source} to {destination}:')
        print(f'    - path: {self.path}')
        print(f'    - weight: {visited[destination][0]}')       

    def dijkstras_shortest_path(self, source, destination):
        # initialisation
        self.unvisited = {}
        self.visited = {}
        INF = 99999999
        for node in self.graph:
            self.unvisited[node] = [INF, None] 
        self.unvisited[source][0] = 0 # set source weight to 0
    
        # loop until all nodes visited
        while len(self.unvisited) > 0:
            current_node = min(self.unvisited, key = self.unvisited.get) # lowest weight node
            neighbours = self.graph[current_node]
