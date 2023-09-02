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

        if x_request_id is not None:
            return x_request_id
        else:
            return None

    except urllib.error.URLError as e:
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id is not None:
        print(x_request_id)
    else:
        print(None)
