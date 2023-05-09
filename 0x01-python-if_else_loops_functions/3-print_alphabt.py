#!/usr/bin/python3
"""
prints the ASCII alphabet, in lowercase,
not followed by a new line, except for q and e.
"""

for letter in range(ord('a'), ord('z')+1):
    if letter != ord('q') and letter != ord('e'):
        print("{:c}".format(letter), end="")
