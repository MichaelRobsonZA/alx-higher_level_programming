#!/usr/bin/python3
"""Contains classes for working with Polygons.
"""


class Base:
    """Represents the base class for polygon objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new polygon object.

        Args:
            id (int): The id of the polygon.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def validate_numeric_input(value, value_name):
        """Validates if a numeric value is greater than 0.

        Args:
            value (int): The numeric value to validate.
            value_name (str): The name of the value being validated.

        Raises:
            ValueError: If the value is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError(f"{value_name} must be greater than 0.")

    @classmethod
    def create(cls, **dictionary):
        """Creates a polygon with the given attributes.

        Args:
            dictionary (dict): A dictionary of the object's attributes.

        Returns:
            Base: A polygon object with the given attributes.
        """
        if cls.__name__ == "Rectangle":
            polygon = cls(1, 1)
        elif cls.__name__ == "Square":
            polygon = cls(1)
        else:
            polygon = cls()
        polygon.update(**dictionary)
        return polygon

    def update(self, *args, **kwargs):
        """Updates the attributes of the polygon object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            ValueError: If there are more than 5 arguments provided.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Creates a dictionary representation of this polygon.

        Returns:
            dict: A dictionary representation of this polygon.
        """
        return {
            "id": self.id
        }

