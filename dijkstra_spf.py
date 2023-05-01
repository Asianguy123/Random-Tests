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
