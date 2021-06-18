# Kruskal's Minimum Spanning Tree Algorithm

# sort edges in ascending weight order #DONE
# pick lowest weight edge #DONE
# pick next edge - add if it doesnt create a cycle 
# print MST and weight


def test_one():
# expected answer = 20
    edges = [['AB', 7],
            ['AD', 6],
            ['AE', 5],
            ['BD', 6],
            ['BC', 5],
            ['CD', 8],
            ['DE', 4]
    ]
    return edges

def test_two():
# expected answer = 64
    edges = [['AB', 15],
            ['AE', 25],
            ['BE', 8],
            ['BF', 11],
            ['BC', 22],
            ['CF', 10],
            ['CD', 14],
            ['DF', 6],
            ['EF', 21]
    ]
    return edges

def test_three():
# expected answer = 37
    edges = [['01', 4],
            ['07', 8],
            ['17', 11],
            ['12', 8],
            ['28', 2],
            ['25', 4],
            ['23', 7],
            ['35', 14],
            ['34', 9],
            ['45', 10],
            ['56', 2],
            ['68', 6],
            ['67', 1],
            ['78', 7]
    ]
    return edges
#, test_two(), test_three()
tests = [test_one()]
for edges in tests:
    nodes = set()
    for edge in edges:
        nodes.add(edge[0][0])
        nodes.add(edge[0][1])
    tree_nodes = set()
    edges.sort(key = lambda x: x[1])
    print(edges)
    for edge in edges:
        print(tree_nodes)
        if len(tree_nodes) == 0:
            tree_nodes.add(edge[0][0])
            tree_nodes.add(edge[0][1])
        elif edge[0][0] in tree_nodes:
            if edge[0][1] in tree_nodes:
                edges.remove(edge)
            else:
                tree_nodes.add(edge[0][1])
        elif edge[0][1] in tree_nodes:
            if edge[0][0] in tree_nodes:
                edges.remove(edge)
        else:
            tree_nodes.add(edge[0][0])
            tree_nodes.add(edge[0][1])
    mst_weight = 0
    for edge in edges:
        connection = f'{edge[0][0]} ---- {edge[0][1]} : Weight = {edge[1]}'
        mst_weight += edge[1]
        print(connection)
    print(edges)
    print(mst_weight)

# currently broken, will return to it at a later date