#!/usr/bin/python3
"""
Module documentation: save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function documentation: save_to_json_file

    Writes an Object to a text file in JSON format.

    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
