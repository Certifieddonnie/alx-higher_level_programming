#!/usr/bin/python3
"""
A Script that takes in a letter and sends a POST
request to 'http://0.0.0.0:5000/search_user' with
the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        val = ""
    else:
        val = argv[1]

    try:
        values = {'q': val}
        r = requests.post(url, data=values)
        if r.json() == {}:
            print("No result")
        else:
            print(f"[{(r.json()).get('id')}] {(r.json()).get('name')}")
    except ValueError:
        print("Not a valid JSON")
