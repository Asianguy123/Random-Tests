# Triangulation 

# determine if a triangle is formed, and what kind, given side lengths

# ---------------------------------------------------------------------------------------------------------------------
# Check Functions

def valid_input(sides):
    for side in sides:
        try:
            val = int(side)
            if val <= 0:
                return False
        except ValueError:
            return False
    return True

def triangle_inequality(a, b, c):
    if (a + b) > c:
        if (b + c) > a:
            if (c + a) > b:
                return True
    return False
