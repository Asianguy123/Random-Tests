# Recursion

# ---------------------------------------------------------------------------------------------------------------------
# Factorial Calculator

def factorial_calc(num):
    '''
    Calculates factorials using iteration
    '''

    out = 1
    if num != 0:
        for i in range(2, num + 1):
            out *= i
    return num

def recursive_factorial_calc(x):
    '''
    Calculates fcatorials using recursion - faster, but can result in a stack overflow
    '''

    if x == 1 or x == 0:
        return 1
    else:
        return x * recursive_factorial_calc(x - 1)

def run_factorial_calc():
    '''
    Input and calls factorial calc function (currently recursive one)
    '''

    num = int(input('Enter the integer you would like to find the factorial of:  '))
    print(recursive_factorial_calc(num))

# ---------------------------------------------------------------------------------------------------------------------
# Tower of Hanoi, disc moving problem

def TOH(n, source, intermediate, destination):
    '''
    Takes number of discs and node labels

    - returns when n = 1
    - calls itself and switches intermediate and destination nodes, creates a recursive loop
    - calls itself again but makes swaps source and intermediate nodes, creates a 2nd recursive loop
    '''

    if n == 1:
        print(f'Move disc 1 from {source} to {destination}')
        return
    TOH(n - 1, source, destination, intermediate)
    print(f'Move disc {n} from {source} to {destination}')
    TOH(n - 1, intermediate, source, destination)


def run_TOH():
    '''
    Input and calls TOH function
    '''

    discs = int(input('Enter the integer number of discs you want in your tower:  '))
    TOH(discs, 'A', 'B', 'C')

if __name__ == '__main__':
    run_TOH()

# ---------------------------------------------------------------------------------------------------------------------
# Tracing recursion for 3 discs:

'''
def TOH(3, A, B, C):
    if n == 1:
        print(f'Move disc 1 from {source} to {destination}')
        return
    TOH(2, A, C, B)

    def TOH(2, A, C, B):
        if n == 1:
            print(f'Move disc 1 from {source} to {destination}')
            return
        TOH(1, A, B, C)

        def TOH(1, A, B, C):
            if n == 1:
                print(f'Move disc 1 from A to C')
                return

        print(f'Move disc 2 from A to B')
        TOH(1, C, A, B)

        def TOH(1, C, A, B):
            if n == 1:
                print(f'Move disc 1 from C to B')
                return

    print(f'Move disc 3 from A to C')
    TOH(2, B, A, C)

    def TOH(2, B, A, C):
        if n == 1:
            print(f'Move disc 1 from {source} to {destination}')
            return
        TOH(1, B, C, A)

        def TOH(1, B, C, A):
            if n == 1:
                print(f'Move disc 1 from B to A')
                return

        print(f'Move disc 2 from B to C')
        TOH(1, A, B, C)

        def TOH(1, A, B, C):
            if n == 1:
                print(f'Move disc 1 from A to C')
                return

1: A => C
2: A => B
1: C => B
3: A => C
1: B => A
2: B => C
1: A => C
'''