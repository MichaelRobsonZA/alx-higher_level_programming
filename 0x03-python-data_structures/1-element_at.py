#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None

# Loop through the list to find the element at the specified index
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
