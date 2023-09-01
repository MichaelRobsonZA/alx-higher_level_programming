#!/usr/bin/python3
"""Fetches and displays the status from a URL using urllib."""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {content.decode('utf-8')}")
