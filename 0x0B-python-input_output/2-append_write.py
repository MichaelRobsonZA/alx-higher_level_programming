#!/usr/bin/python3
"""
function that appends a string anf returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
