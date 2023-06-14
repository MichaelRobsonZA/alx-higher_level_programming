#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The content to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

