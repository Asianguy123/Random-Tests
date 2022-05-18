# Testing recursive functions using classic examples:

# Factorial calculation
# Tower of Hanoi logic problem

# ---------------------------------------------------------------------------------------------------------------------
# Factorial Calculator

def factorial_calc(num):
    out = 1
    if num != 0:
        for i in range(2, num + 1):
            out *= i
    return num
