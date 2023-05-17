#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(roman_string)
    total = roman_dict[roman_string[n-1]]
    for i in range(n-2, -1, -1):
        if roman_dict[roman_string[i]] >= roman_dict[roman_string[i+1]]:
            total += roman_dict[roman_string[i]]
        else:
            total -= roman_dict[roman_string[i]]
    return total
