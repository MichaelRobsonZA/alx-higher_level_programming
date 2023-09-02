#!/usr/bin/python3
"""
POST request with an email parameter to a URL and displays the response body.
"""
import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Your email is:", response.text)
    else:
        print("Failed to post email.")
        print("HTTP status code:", response.status_code)
