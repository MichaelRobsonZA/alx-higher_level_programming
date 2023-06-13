#!/usr/bin/python3
"""
Module: 4-from_json_string
Contains:
    - from_json_string
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
