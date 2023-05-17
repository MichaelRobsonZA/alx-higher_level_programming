#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.
    Args:
        set_1 (set): A set of elements.
        set_2 (set): Another set of elements.
    Returns:
        set: A new set containing the common elements between set_1 and set_2.
    """
    return set_1 & set_2
