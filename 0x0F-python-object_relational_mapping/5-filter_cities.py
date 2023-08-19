#!/usr/bin/python3
"""
Reads a file, appends a string to it, and saves the changes.
"""

import sys

def manipulate_file(file_name, string_to_append):
    try:
        # Open the file in append mode
        with open(file_name, "a") as file:
            file.write(string_to_append + "\n")
        print("String appended to the file successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <file_name> <string_to_append>".format(sys.argv[0]))
        sys.exit(1)
    
    file_name = sys.argv[1]
    string_to_append = sys.argv[2]

    manipulate_file(file_name, string_to_append)
