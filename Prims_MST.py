# Prim's Minimum Spanning Tree Algorithm

'''
Choose any start vertex
Select an edge of least weight that joins a new vertex to the tree
    => if equal edges, pick any
- Repeat until all vertices added
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
# Prim's + Distance Matrix Creation Functions

def make_distance_matrix(edges, vertices):
    '''
    Converts given network into a distance matrix
        - each index represents the node connection e.g. dist_matrix[0][5] is the connection from node 0 to node 5
    '''

    dist_matrix = [[0 for x in range(vertices)] for i in range(vertices)]
    for edge in edges:
        dist_matrix[edge[1]][edge[2]] = edge[0]
        dist_matrix[edge[2]][edge[1]] = edge[0]
    return dist_matrix

def prims(dist_matrix, vertices):
    '''
    Implements Prim's MST algorithm
        - runs until vertices - 1 has been added to graph
        - works by reducing minimum value until lowest edge found in that loop
    '''

    MST_weight = 0
    BIG_NUM = 999999999
    edge_count = 0
    nodes = [0 for x in range(vertices)]
    nodes[0] = True
    while edge_count < (vertices - 1):
        minimum = BIG_NUM
        node_one, node_two = 0, 0
        for i in range(vertices):
            if nodes[i]:
                for j in range(vertices):
                    if ((not nodes[j]) and dist_matrix[i][j] > 0):
                        if minimum > dist_matrix[i][j]:
                            minimum = dist_matrix[i][j]
                            node_one, node_two = i, j
        MST_weight += dist_matrix[node_one][node_two]
        nodes[node_two] = True
        edge_count += 1
        print(f'{node_one} --- {node_two}: weight {dist_matrix[node_one][node_two]}')
    return MST_weight

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def run_prims():
    '''
    Run Prim's MST algorithm on the given tests
    '''

    tests = [test_one, test_two, test_three]
    for test in tests:
        vertices, edges = test()
        dist_matrix = make_distance_matrix(edges, vertices)
        MST_weight = prims(dist_matrix, vertices)
        print(f'\nMST weight: {MST_weight}\n\n')
        
# ---------------------------------------------------------------------------------------------------------------------
# Runs Program

if __name__ == '__main__':
    run_prims()
