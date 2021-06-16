# Kruskal's Minimum Spanning Tree Algorithm

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