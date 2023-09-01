#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)
content = response.text

print("Your email is:", content)
