#!/usr/bin/python3

def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        print(file.read(), end='')
