#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for value in my_list:
        result.append(value % 2 == 0)
    return result
