#!/usr/bin/python3
import requests
import sys

url, email = sys.argv[1], sys.argv[2]
data = {'email': email}

response = requests.post(url, data=data)
print("Your email is:", response.text)
