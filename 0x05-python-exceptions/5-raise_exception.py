#!/usr/bin/python3
"""
Raise exception
"""


def raise_exception():
    """
    Raises a type exception
    """
    raise TypeError


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
