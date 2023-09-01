#!/usr/bin/python3
"""
Takes a URL as input, sends a request, and displays the response content.
If the status code is >= 400, it prints the error code.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
