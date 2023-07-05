# Bubble, Insertion, Merge and Quick Sort Algorithms

# ---------------------------------------------------------------------------------------------------------------------
# Bubble Sort

def bubble_sort(array):
    '''
    Bubble Sort
    
    - compares each pair of values
    - in each pass the next largest unsorted value is correctly indexed
    - passes done until no swaps are made
    - time = O(n^2)
    - space = O(1)
    '''

    for i in range(len(array)):
        swap = False # swap flag

        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                swap = True
                temp_val = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp_val

        if not swap: # if swap = False after a pass then sort is done
            return array
        
# ---------------------------------------------------------------------------------------------------------------------
# Insertion Sort

def insertion_sort(array):
    '''
    Insertion Sort

    - compares with the previous value
    - guarantees that with n passes that the first n + 1 elements of the list are ordered
    - passes done until all indices (except i=0) have been checked
    - time = O(n^2)
    - space = O(1)
    '''

    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array

# ---------------------------------------------------------------------------------------------------------------------
# Merge Sort

def merge_sort(array):
    '''
    Merge Sort

    - divide and conquer into single element lists
    - combine lists whilst sorting to create the full sorted lists
    - recursive algorithm
    - time = O(nlogn)
    - space = O(n)
    '''

    if len(array) > 1:
        # recursively splitting the array until length of 1
        splice_point = len(array) // 2
        left = array[:splice_point]
        right = array[splice_point:]
        merge_sort(left)
        merge_sort(right)

        # merging arrays
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        # if len(left) != len(right)
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1  
    return array

# ---------------------------------------------------------------------------------------------------------------------
# Quick Sort

def quick_sort(array):
    '''
    Quick Sort

    - compare and swap values, moving inwards until a pivot is determined
    - split the array at the pivot and repeat until lists of a single element
    - time = O(n^2) worst case, average O(nlogn)
    - space = O(logn), as it uses a stack

    '''

    def find_pivot(array, left, right):
        '''
        finds the pivot point by swapping values and moving inwards
        '''

        zero = array[right]
        one = left - 1
        for i in range(left, right):
            if array[i] <= zero:
                one += 1
                array[one], array[i] = array[i], array[one]
        array[one + 1], array[right] = array[right], array[one + 1]
        return i + 1
    
    def recursive_qs(array, left, right):
        '''
        recursively creates pivots in the array until only single elements are left
        '''
        
        if left < right:
            pivot = find_pivot(array, left, right)
            recursive_qs(array, left, pivot - 1)
            recursive_qs(array, pivot + 1, right)
        return array
    
    return recursive_qs(array, 0, len(array) - 1)
