#!/usr/bin/python3
"""
POST request email parameter to a URL and displays the response body.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data)

        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.URLError as e:
        print("Error: {}".format(e))
        sys.exit(1)
