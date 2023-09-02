#!/usr/bin/python3
"""
Uses the GitHub API to display your GitHub user ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <MichaelRobsonZA> <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>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {
        'Authorization': 'token {}'.format(token)
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get('id')
            print(user_id)
        else:
            print("None")

    except Exception as e:
        print("None")
