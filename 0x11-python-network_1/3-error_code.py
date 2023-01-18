#!/usr/bin/python3
"""
A Script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
"""
import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")