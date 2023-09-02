#!/usr/bin/python3
"""
Fetches the X-Request-Id variable from the header of a URL response.
"""

import urllib.request
import sys

def get_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')

        return x_request_id  # Return the value, even if it's None

    except urllib.error.URLError as e:
        return None  # Return None when there's an error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
