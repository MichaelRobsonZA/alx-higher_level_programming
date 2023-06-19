#!/usr/bin/python3
"""
This module defines the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class.
    """

    def __init__(self, size, x=0, y=0):
        """
        Initializes the Square instance.
        Args:
            size (int): The size of the instance.
            x (int): The x-coordinate of the instance's position (default: 0).
            y (int): The y-coordinate of the instance's position (default: 0).
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        Returns:
            A string representing the instance.
        """
        return f"Square({self.width})"

    def __repr__(self):
        """
        Returns a string representation of the Square instance
        that can be used to recreate the instance.
        Returns:
            A string representing the instance.
        """
        return f"Square({self.width})"
