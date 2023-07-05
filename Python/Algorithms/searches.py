# Linear and Binary searches

def linear_search(array, element):
    '''
    Linear search:
    - can be performed on unsorted lists
    - using a flag (for demonstrative purposes)
    - time = O(n)
    '''

    i = 0
    flag = False
    while not flag:
        if i == len(array):
            return 'Element not in array'
        if array[i] == element:
            return i
        i += 1

def binary_search(array, element):
    '''
    Binary search:
    - performed only on sorted data (this function accepts unsorted too)
    - uses a flag (for demonstrative purposes)
    - time = O(logn)
    '''

    array = sorted(array)
    flag = False
    index = 0
    while not flag:
        i = len(array) // 2
        if array[i] == element:
            index += i
            flag = True
        if i == 0:
            return 'Element not in array'
        if array[i] < element:
            index += i
            array = array[i:]
        elif array[i] > element:
            array = array[:i] 
    return index
