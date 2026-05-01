"""Functions determining triangle nature."""

def equilateral(sides):
    """Determine if triangle is equilateral."""
    a = sides[0]
    b = sides[1]
    c = sides[2]    
    return a == b == c and a + b == 2 * c and sides != [0, 0, 0]


def isosceles(sides):
    """Determine if triangle is isoceles."""
    a = sides[0]
    b = sides[1]
    c = sides[2]   
    return a + b >= c and b + c >= a and a + c >= b and (a == b or b == c or a == c)


def scalene(sides):
    """Determine if triangle is scalene."""
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return  a + b >= c and b + c >= a and a + c >= b and (not equilateral(sides) and not isosceles(sides))