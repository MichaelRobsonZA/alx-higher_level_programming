#!/usr/bin/python3
"""Defines a function that checks inherited directly, indirectly)from class"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
