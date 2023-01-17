#!/bin/bash
# A Script that takes in a URL, sends a request to that URL, and displays the size of th body of the response.
curl -sI "$1" | wc -c
