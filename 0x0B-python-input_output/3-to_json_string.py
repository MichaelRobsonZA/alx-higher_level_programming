#!/usr/bin/python3
"""Module to convert an object to a JSON string"""

import json


def to_json_string(my_obj):
    """
    Converts an object to a JSON string.

    Args:
        my_obj: The object to be converted.

    Returns:
        The JSON string representation of the object.
    """
    return json.dumps(my_obj)
