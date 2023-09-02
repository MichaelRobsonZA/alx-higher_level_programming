#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id variable in the response header of a URL.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    if "X-Request-Id" in response.headers:
        x_request_id = response.headers["X-Request-Id"]
        print(x_request_id.strip())
    else:
        print(None)
