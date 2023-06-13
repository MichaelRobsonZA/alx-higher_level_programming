#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it to stdout.
"""

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
