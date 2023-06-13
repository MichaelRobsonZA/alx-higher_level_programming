#!/usr/bin/python3
"""
Module that adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os.path
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str]) -> None:
    """
    Function that adds all arguments to a list and saves them to a JSON file.

    Args:
        args (List[str]): The list of arguments.

    Returns:
        None.
    """
    filename = "add_item.json"
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:])
