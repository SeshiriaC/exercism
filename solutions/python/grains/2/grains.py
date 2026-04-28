def square(number):
    if number < 1:
        raise ValueError("square must be between 1 and 64")
    if number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    number_of_grains = 0
    for i in range (1, 65):
        number_of_grains = number_of_grains + square(i)
    return number_of_grains
