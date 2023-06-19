#!/usr/bin/python3
"""
This module defines the Base class.
"""


class Base:
    """
    The Base class.
    """

    def __init__(self, width, height):
        """
        Initializes the Base instance.
        Args:
            width (int): The width of the instance.
            height (int): The height of the instance.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the Base instance.
        Returns:
            The area of the instance.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the Base instance.
        Returns:
            The perimeter of the instance.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the Base instance.
        Returns:
            A string representing the instance.
        """
        return f"Base({self.width}, {self.height})"

    def __repr__(self):
        """
        Returns a string representation of the Base instance
        that can be used to recreate the instance.
        Returns:
            A string representing the instance.
        """
        return f"Base({self.width}, {self.height})"

