# Binary Exponentiation

# Binary Exponentiation

'''
Binary exponentiation is a method of reducing the time complexity when calculating large exponential values a^n e.g. 3^139

It reduces the standard method of multiplying a, n times with O(n) time complexity to a O(log2(n))
It works by using converting n to binary form and adding powers of a that are much quicker to compute

Example of 3^139:

    standard approach takes 139 iterations: 3 * 3 * 3 .....

    bin_exp takes 1 + floor(log2(n)) iterations (how many bits n can be represented within): 1 + 7 = 8 iterations

Has applications within modular exponentiation, calculating fibonacci numbers and applying repeated linear transformations 
'''

import numpy

def bin_exp(a, n):
    '''
    Basic binary exponentiation
    '''

    r = 1
    while n:
        if n % 2 == 1:
            r *= a
        a *= a
        n = n // 2
    return r
