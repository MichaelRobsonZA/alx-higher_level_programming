#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the response.
It uses the packages urllib and sys.
"""

import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
