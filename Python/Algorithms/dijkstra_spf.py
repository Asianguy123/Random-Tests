# Dijkstra's Shortest Pathfinding Algorithm

class Graph:

    '''
    GRAPH CLASS:

    - create a graph using a dictionary
    - display shortest path found with Dijkstra's
    - implementation of Dijkstra's
    '''
     
    def __init__(self, graph):
        self.graph = graph

    def get_path(self, visited, source, destination):
        '''
        Back tracks from destination node, using previous node data until source node is reached
        '''

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
        '''
        Implementation of Dijkstra's algorithm on the Graph instance
        '''

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

            # compares neighbour routes to decide on next node to visit
            for node in neighbours:
                if node not in self.visited:
                    weight = self.unvisited[current_node][0] + neighbours[node]
                    if weight < self.unvisited[node][0]:
                        self.unvisited[node][0] = weight
                        self.unvisited[node][1] = current_node
            self.visited[current_node] = self.unvisited[current_node] # current node declared as visited
            del self.unvisited[current_node]
        self.get_path(self.visited, source, destination)      

# ---------------------------------------------------------------------------------------------------------------------
# Run Program

graph = {
        "A": {"B":8, "C":5},
        "C": {"A":5, "D":6, "E":9},
        "B": {"A":8, "D":1},
        "D": {"C":6, "B":1, "E":2},
        "E": {"C":9, "D":2}
        }

if __name__ == '__main__':
    g = Graph(graph)
    g.dijkstras_shortest_path('A', 'C')