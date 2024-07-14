#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
If an HTTPError occurs, it prints "Error code:" followed by HTTP status code.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Fetches the content of the URL and prints
    the body of response (decoded in utf-8).
    If an HTTPError occurs, it prints "Error code:"
    followed by the HTTP status code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
