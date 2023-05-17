#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    Args:
        a_dictionary (dict): A dictionary.
        key: The key to replace or add.
        value: The new value for the key.
    Returns:
        dict: A new dictionary with the updated key/value pair.
    """
    a_dictionary[key] = value
    return a_dictionary
