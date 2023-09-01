#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status.
It uses the package urllib.
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
    print("    - utf8 content:", content.decode("utf-8"))

