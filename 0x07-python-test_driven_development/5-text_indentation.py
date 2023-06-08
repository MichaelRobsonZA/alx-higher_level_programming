#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If text is not a string

    Returns:
        None
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    punctuations = ".?:"
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in punctuations:
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
