#!/usr/bin/python3
"""
Module containing the Base class.
"""

class Base:
    """
    The base class for all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.
        Args:
            id (int): The identifier of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

