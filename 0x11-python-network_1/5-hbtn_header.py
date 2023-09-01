#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
header = response.headers
x_request_id = header.get("X-Request-Id")

print(x_request_id)
