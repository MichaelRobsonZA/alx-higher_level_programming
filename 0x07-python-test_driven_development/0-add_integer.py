#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
