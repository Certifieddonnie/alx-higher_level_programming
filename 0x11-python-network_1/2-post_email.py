#!/usr/bin/python3
"""
A Script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a
parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    # print(req)
    with urllib.request.urlopen(url, data) as response:
        page = response.read()
        print(page.decode('utf-8'))
