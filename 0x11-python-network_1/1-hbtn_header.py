#!/usr/bin/python3
"""Displays the X-Request-id header variable of a request to a given URL."""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-id')
        print(x_request_id)
