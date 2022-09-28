# Kruskal's Minimum Spanning Tree Algorithm

'''
- sort edges in ascending weight order
- pick lowest weight edge
- pick next edge - add if it doesnt create a cycle 
- print MST and weight
'''

# network contruction format: [[weight, node_one, node_two], []...] ==> all integers with (0 indexing for nodes)

# ---------------------------------------------------------------------------------------------------------------------
# Tests

def test_one():
    '''
    expected MST weight = 20
    connections:    3-4, 0-4, 1-2, 1-3
    '''

    vertices = 5
    edges = [[7, 0, 1],
            [6, 0, 3],
            [5, 0, 4],
            [6, 1, 3],
            [5, 1, 2],
            [8, 2, 3],
            [4, 3, 4]
    ]
    return vertices, edges

def test_two():
    '''
    expected MST weight = 50
    connections:    3-5, 1-4, 2-5, 1-5, 0-1
    '''

    vertices = 6
    edges = [[15, 0, 1],
            [25, 0, 4],
            [8, 1, 4],
            [11, 1, 5],
            [22, 1, 2],
            [10, 2, 5],
            [14, 2, 3],
            [6, 3, 5],
            [21, 4, 5]
    ]
    return vertices, edges

def test_three():
    '''
    expected MST weight = 37
    connections:    6-7, 2-8, 5-6, 0-1, 2-5, 2-3, 0-7, 3-4
    '''

    vertices = 9
    edges = [[4, 0, 1],
            [8, 0, 7],
            [11, 1, 7],
            [8, 1, 2],
            [2, 2, 8],
            [4, 2, 5],
            [7, 2, 3],
            [14, 3, 5],
            [9, 3, 4],
            [10, 4, 5],
            [2, 5, 6],
            [6, 6, 8],
            [1, 6, 7],
            [7, 7, 8]
    ]
    return vertices, edges

# ---------------------------------------------------------------------------------------------------------------------
# Graph Class

class Graph():

    '''
    GRAPH CLASS:

    - create a graph of N vertices
    - add x edges
    - Union Find algorithm, to check for and avoid cycles
    - returns a list of edges that form the MST + its weight
    '''

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, edge):
        self.graph.append(edge)

    # Union Find algorithm

    def find(self, parent_set, i):
        '''
        Finds if 2 nodes are in the same set
        '''

        if parent_set[i] == i:
            return i
        return self.find(parent_set, parent_set[i])

    def union(self, parent_set, ranks, node_one, node_two):
        '''
        Combines 2 subsets into a single set
        '''

        n1_root = self.find(parent_set, node_one)
        n2_root = self.find(parent_set, node_two)
        if ranks[n1_root] < ranks[n2_root]:
            parent_set[n1_root] = n2_root
        elif ranks[n1_root] > ranks[n2_root]:
            parent_set[n2_root] = n1_root
        else:
            parent_set[n2_root] = n1_root
            ranks[n1_root] += 1

    # Kruskal's Algorithm

    def kruskals(self):
        mst = []
        i = 0
        j = 0
        self.graph = sorted(self.graph, key=lambda edge:edge[0])
        parent_set = []
        ranks = []
        for vertex in range(self.vertices):
            parent_set.append(vertex)
            ranks.append(0)
        while j < (self.vertices - 1):
            edge = self.graph[i]
            i += 1
            node_one = self.find(parent_set, edge[1])
            node_two = self.find(parent_set, edge[2])
            if node_one != node_two:
                j += 1
                mst.append(edge)
                self.union(parent_set, ranks, node_one, node_two)
        return mst

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def run_kruskal():
    tests = [test_one, test_two, test_three]
    for test in tests:
        vertices, edges = test()
        network = Graph(vertices)
        for edge in edges:
            network.add_edge(edge)
        mst = network.kruskals()
        mst_weight = 0
        for edge in mst:
            mst_weight += edge[0]
            print(f'{edge[1]} --- {edge[2]}: weight {edge[0]}')
        print(f'\nMST weight: {mst_weight}\n\n')


# ---------------------------------------------------------------------------------------------------------------------
# Runs Program

if __name__ == '__main__':
    run_kruskal()

'''
Notes:

need a way of cycle checking
=> union find algorithm 
    - finds what subset an element is in, then joins 2 subsets into a single subset if they are from the same set

if from same set, can ignore that edge and move onto next lowest weight edge
'''
