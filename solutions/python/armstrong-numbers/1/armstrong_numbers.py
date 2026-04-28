def is_armstrong_number(number):
    """Return True if a number is an armstrong number."""
    number_in_string =  str(number)
    power_number = len(number_in_string)
    total = 0

    for unit in number_in_string:
        total = total + int(unit) ** power_number
    
    return total == number

