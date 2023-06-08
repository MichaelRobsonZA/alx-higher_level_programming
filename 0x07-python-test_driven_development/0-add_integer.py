#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added. Default is 98.

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
