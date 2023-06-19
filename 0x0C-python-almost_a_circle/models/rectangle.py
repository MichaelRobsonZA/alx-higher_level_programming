#!/usr/bin/python3
"""Contains classes for working with Polygons.
"""
from .base import Base


class Rectangle(Base):
    """Represents a rectangle, which is a polygon with four sides and four right angles.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal position of the rectangle.
            y (int): The vertical position of the rectangle.
            id (int): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Displays the rectangle using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Creates a string representation of this rectangle.

        Returns:
            str: A string representation of this rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

