#!/usr/bin/python3
"""
Module that defines a function to load objects from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        The Python object represented by the JSON file.

    """
    with open(filename, 'r') as file:
        return json.load(file)
