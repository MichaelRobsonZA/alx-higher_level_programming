#!/usr/bin/python3
"""
Simulates a restricted access situation.
"""

import sys

# Dictionary of valid credentials
valid_credentials = {
    "user1": "password123",
    "user2": "qwerty456",
    "user3": "letmein789"
}

def grant_access(username, password):
    if username in valid_credentials and valid_credentials[username] == password:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <password>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]

    if grant_access(username, password):
        print("Access granted!")
    else:
        print("Access denied!")
