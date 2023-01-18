#!/usr/bin/python3
"""
A Script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    verify = HTTPBasicAuth(username=username, password=password)
    r = requests.get(url, auth=verify)
    print(r.json().get('id'))
