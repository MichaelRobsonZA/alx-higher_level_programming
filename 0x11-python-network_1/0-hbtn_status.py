#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package
and displays information about the response content.
"""

import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content_type = type(response.text).__name__
    utf8_content = response.text

    print("Body response:")
    print(f"    - type: {content_type}")
    print(f"    - content: {utf8_content}")
