#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()
    content = response.text
    print(content)
except requests.exceptions.HTTPError as e:
    print("Error code:", e.response.status_code)
