"""Collatz Conjecture"""
def steps(number):
    """ Return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    
    while number > 1:
        if number % 2 == 0 :
            number = number / 2
            step += 1
        else :
            number = number * 3 + 1
            step += 1
    return step

    
