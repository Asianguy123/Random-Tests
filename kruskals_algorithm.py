# Kruskal's Minimum Spanning Tree Algorithm

'''
- sort edges in ascending weight order #DONE
- pick lowest weight edge #DONE
- pick next edge - add if it doesnt create a cycle 
- print MST and weight
'''

# network contruction: [[weight, 'node', 'node']]


def test_one():
# expected answer = 20
    edges = [[7, 'A', 'B'],
            [6, 'A', 'D'],
            [5, 'A', 'E'],
            [6, 'B', 'D'],
            [5, 'B', 'C'],
            [8, 'C', 'D'],
            [4, 'D', 'E']
    ]
    return edges

def test_two():
# expected answer = 50
    edges = [[15, 'A', 'B'],
            [25, 'A', 'E'],
            [8, 'B', 'E'],
            [11, 'B', 'F'],
            [22, 'B', 'C'],
            [10, 'C', 'F'],
            [14, 'C', 'D'],
            [6, 'D', 'F'],
            [21, 'E', 'F']
    ]
    return edges

def test_three():
# expected answer = 37
    edges = [[4, '0', '1'],
            [8, '0', '7'],
            [11, '1', '7'],
            [8, '1', '2'],
            [2, '2', '8'],
            [4, '2', '5'],
            [7, '2', '3'],
            [14, '3', '5'],
            [9, '3', '4'],
            [10, '4', '5'],
            [2, '5', '6'],
            [6, '6', '8'],
            [1, '6', '7'],
            [7, '7', '8']
    ]
    return edges


# Define the node set with the global variable X, which is similar to {'A':'A','B':'B','C':'C','D':'D'}, if A and B are two If the points are connected, it will be changed to {'A':'B','B':'B",...}, that is, after any two points are connected, the value of the two points will be the same.
x = dict()
r = dict() # The initial level of each point is 0, if it is used as the end of the connection, increase by 1

def make_set(point):
    x[point] = point
    r[point] = 0

def find(point):
    if x[point] != point:
        x[point] = find(x[point])
    return x[point]

def merge(point1, point2):
    '''Connect two components (nodes)
    '''
    r1 = find(point1)
    r2 = find(point2)
    if r1 != r2:
        if r[r1] > r[r2]:
            x[r2] = r1
        else:
            x[r1] = r2
            if r[r1] == r[r2]:
                r[r2] += 1

def kruskal(vertices,edges):
    '''Kruskal algorithm implementation
    '''
    for vertice in vertices:
        make_set(vertice)
    tree = []
    mst_weight = 0
    edges.sort()  # Sort by weight from smallest to largest
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            merge(vertice1, vertice2)
            tree.append(edge)
            mst_weight += weight
    return tree, mst_weight

tests = [test_one(), test_two(), test_three()]
for edges in tests:
    vertices = set()
    for edge in edges:
        vertices.add(edge[1])
        vertices.add(edge[2])
    tree, tree_weight = kruskal(list(vertices), edges)
    for i in tree:
        print(f'{i[1]} ---- {i[2]}: Weight = {i[0]}')
    print(f'\nMinimum Spanning Tree Weight: {tree_weight}\n\n')

