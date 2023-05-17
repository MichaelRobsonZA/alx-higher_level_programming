#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    best_key = ""
    best_value = -1
    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value
    return best_key
