"""Functions determining triangle nature."""

def equilateral(sides):
    """Determine if triangle is equilateral."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]    
    return side_1 == side_2 == side_3 and side_1 + side_2 == 2 * side_3 and sides != [0, 0, 0]


def isosceles(sides):
    """Determine if triangle is isoceles."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]   
    return side_1 + side_2 >= side_3 and side_2 + side_3 >= side_1 and side_1 + side_3 >= side_2 and (side_1 == side_2 or side_2 == side_3 or side_1 == side_3)


def scalene(sides):
    """Determine if triangle is scalene."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    return  side_1 + side_2 >= side_3 and side_2 + side_3 >= side_1 and side_1 + side_3 >= side_2 and (not equilateral(sides) and not isosceles(sides))