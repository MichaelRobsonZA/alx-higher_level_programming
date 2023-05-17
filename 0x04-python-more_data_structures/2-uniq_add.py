#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    Args:
        my_list (list): A list containing integers.
    Returns:
        int: The sum of all unique integers in my_list.
    """
    return sum(set(my_list))
