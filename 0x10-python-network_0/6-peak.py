#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None

    def _find_peak(list_of_integers, start, end):
        if start >= end:
            return list_of_integers[start]

        mid = (start + end) // 2
        left = _find_peak(list_of_integers, start, mid - 1)
        right = _find_peak(list_of_integers, mid + 1, end)

        return left if left >= right else right

    return _find_peak(list_of_integers, 0, len(list_of_integers) - 1)
