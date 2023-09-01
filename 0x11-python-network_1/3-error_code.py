#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the
body of the response (decoded in utf-8). It manages urllib.error.HTTPError
exceptions and prints: "Error code:" followed by the HTTP status code.
It uses the packages urllib and sys.
"""

import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        print(content)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
