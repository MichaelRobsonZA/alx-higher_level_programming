#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance.
        Args:
            width (int): The width of the instance.
            height (int): The height of the instance.
        """
        super().__init__(width, height)

    def display(self):
        """
        Displays the Rectangle instance as a rectangle of '#' characters.
        """
        for _ in range(self.height):
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle instance with new values.
        Args:
            *args: Variable arguments in the order:
                - 1st argument: new width value
                - 2nd argument: new height value
                - 3rd argument: new x value (ignored in this task)
                - 4th argument: new y value (ignored in this task)
            **kwargs: Variable keyword arguments:
                - width: new width value
                - height: new height value
                - x (ignored in this task)
                - y (ignored in this task)
        """
        if args:
            num_args = len(args)
            if num_args > 0:
                self.width = args[0]
            if num_args > 1:
                self.height = args[1]
        else:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']

