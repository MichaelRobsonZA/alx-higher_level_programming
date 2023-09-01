#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using the requests
package.
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
content = response.text

print("Body response:")
print("    - type:", type(content))
print("    - content:", content)
