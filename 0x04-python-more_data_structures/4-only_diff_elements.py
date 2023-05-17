#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    Args:
        set_1 (set): A set of elements.
        set_2 (set): Another set of elements.
    Returns:
set: A new set the elements that are present in only one of the input sets.
    """
    return set_1 ^ set_2
