# Triangulation 

# determine if a triangle is formed, and what kind, given side lengths

# ---------------------------------------------------------------------------------------------------------------------
# Check Functions

def valid_input(sides):
    '''
    Checks if input for side lengths are valid
    '''

    for side in sides:
        try:
            val = int(side)
            if val <= 0:
                return False
        except ValueError:
            return False
    return True

def triangle_inequality(a, b, c):
    '''
    Performs the triangle inequality to check if the inputted sides can form a triangle
    '''

    if (a + b) > c:
        if (b + c) > a:
            if (c + a) > b:
                return True
    return False

def pythagoras(sides):
    '''
    Tests if a set of sides fulfils the Pythagorean Theorem
    '''

    c = max(sides)
    sides.remove(c)
    if int(c)^2 == int(sides[0])^2 + int(sides[1])^2:
        return True
    return False

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def triangulation():
    '''
    Main function, calls other check functions and manages input/output
    '''

    while True:
        a = input('\n\nEnter a side length:  ')
        b = input('Enter a side length:  ')
        c = input('Enter a side length:  ')
        sides = [a, b, c]
        if valid_input(sides):
            a, b, c = int(sides[0]), int(sides[1]), int(sides[2])
            if triangle_inequality(a, b, c):
                if a == b == c:
                    print(outputs[0])
                elif a == b or a == c or b == c:
                    print(outputs[1])
                elif pythagoras(sides):
                    print(outputs[2])
                else:
                    print(outputs[3])
            else:
                print(outputs[4])
        else:
            print(outputs[5])

# ---------------------------------------------------------------------------------------------------------------------
# Outputs

outputs = [
            '\nEquilateral',
            '\nIsosceles',
            '\nRight angled',
            '\nScalene',
            '\nNot a triangle',
            '\nInvalid input',
        ]

# ---------------------------------------------------------------------------------------------------------------------
# Runs Program

if __name__ == '__main__':
    triangulation()