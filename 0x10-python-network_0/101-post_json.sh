#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

json_file="$2"

if [ ! -f "$json_file" ]; then
    echo "Error: JSON file '$json_file' not found."
    exit 1
fi

response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$1")

# Check if the response is valid JSON
if echo "$response" | jq . >/dev/null 2>&1; then
    echo "Valid JSON"
    echo "$response" | jq .
else
    echo "Not a valid JSON"
fi
