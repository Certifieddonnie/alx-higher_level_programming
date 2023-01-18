#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a
request to the URL and displays the body of the
response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        r = requests.get(url)
        print(r.text)
