#!/usr/bin/python3
"""
POST request with an email parameter to a URL and displays the response body.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url, email = sys.argv[1], sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(response.text.strip())  # Print the response body directly
    else:
        print("Failed to post email.")
        print("HTTP status code:", response.status_code)
