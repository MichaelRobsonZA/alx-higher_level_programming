#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Returns dictionary description of data structure JSON serialization"""

    return obj.__dict__
