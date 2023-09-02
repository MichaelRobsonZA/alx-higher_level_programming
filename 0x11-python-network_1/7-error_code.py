#!/usr/bin/python3
"""
HTTP status code is greater than or equal to 400, prints error message.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
