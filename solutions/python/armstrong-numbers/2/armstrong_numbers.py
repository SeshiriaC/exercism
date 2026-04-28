"""Test if a given number is an Armstrong number or not.

Note: 
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. 
"""

def is_armstrong_number(number):
    """Return True if a number is an armstrong number."""
    number_in_string =  str(number)
    power_number = len(number_in_string)
    total = 0

    for unit in number_in_string:
        total = total + int(unit) ** power_number
    
    return total == number