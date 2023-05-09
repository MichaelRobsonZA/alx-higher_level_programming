#!/usr/bin/python3
"""
prints the ASCII alphabet, in lowercase,
not followed by a new line.
"""

for letter in range(ord('a'), ord('z')+1):
    print("{:c}".format(letter), end="")
