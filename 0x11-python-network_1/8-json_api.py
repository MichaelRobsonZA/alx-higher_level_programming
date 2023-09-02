#!/usr/bin/python3
import requests
import sys

letter = sys.argv[1] if len(sys.argv) > 1 else ""
url = "http://0.0.0.0:5000/search_user"
data = {"q": letter}
try:
    response = requests.post(url, data=data)
    response_data = response.json()
    if "id" in response_data and "name" in response_data:
        print("[{}] {}".format(response_data["id"], response_data["name"]))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
