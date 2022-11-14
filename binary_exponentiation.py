# Binary Exponentiation

'''
Binary exponentiation is a method of reducing the time complexity when calculating large exponential values a^n e.g. 3^139

It reduces the standard method of multiplying a, n times with O(n) time complexity to a O(log2(n))
It works by converting n to binary form and adding powers of a that are much quicker to compute

Example of 3^139:

    standard approach takes 139 iterations: 3 * 3 * 3 .....

    bin_exp takes 1 + floor(log2(n)) iterations (how many bits n can be represented within): 1 + 7 = 8 iterations

Has applications within modular exponentiation, calculating fibonacci numbers and applying repeated linear transformations 
'''

import numpy
from math import log10

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

def mod_exp(a, n, m):
    '''
    Modular exponentiation: a^n mod m where a, n, m > 0

    Modular multiplication is distributive => (a * b) mod m = ((a mod m) * (b mod m)) mod m
        => this lets binary exponentiation be implemented to complete modular exponentiation
    '''

    a = a % m
    r = 1
    while n:
        if n % 2 == 1:
            r = (r * a) % m
        a = (a ** 2) % m
        n = n // 2
    return r

def nth_fib(n):
    '''
    Calculating the nth Fibonacci number

    Fibonacci numbers can be calculated using a matrix exponential of the 2x2 matrix (1, 1, 1, 0)^n @ (F1, F2) which is (0, 1)
    Binary exponentiation can be applied to the (1, 1, 1, 0)^n term
    '''

    A = numpy.array([[1, 1], [1, 0]], dtype=object)
    R = numpy.eye(A.shape[0], dtype=object) # identity matrix
    while n:
        if n % 2 == 1:
            R = R @ A
        A = A @ A
        n = n // 2
    return R[1, 0]

def digits(num):
    return int(log10(num) // 1)


if __name__ == '__main__':
    print(bin_exp(37, 1735663))
    print(mod_exp(506144622821207, 36206627334623635837127, 37886293))
    fibonacci_num = nth_fib(10000000)
    print(fibonacci_num)
    print(f'digits: {digits(fibonacci_num)}')
