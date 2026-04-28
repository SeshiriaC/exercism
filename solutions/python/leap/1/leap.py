"""Leap year."""

def leap_year(year):
    """Tells you if the given year is a leap one or not."""
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0