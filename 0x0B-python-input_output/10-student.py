#!/usr/bin/python3
"""
class Student that defines a student by their first name, last name, and age.
"""


class Student:
    """
    Defines a student by their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If list of strings,attribute names contained in the list are retrieved.
        Otherwise, all attributes are retrieved.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
