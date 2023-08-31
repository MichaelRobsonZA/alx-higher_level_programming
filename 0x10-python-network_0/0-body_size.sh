#!/bin/bash
# Get the byte size of the HTTP header for the URL.
curl -s "$1" | wc -c
