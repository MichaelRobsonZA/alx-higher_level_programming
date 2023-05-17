#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    Args:
        a_dictionary (dict): A dictionary.
        key: The key to delete.
    Returns:
        dict: A new dictionary without the deleted key.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
