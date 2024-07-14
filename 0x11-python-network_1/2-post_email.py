#!/usr/bin/python3
"""Script that sends a POST request to a URL with an email
as a parameter and displays the response body.
"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """Send a POST request to the provided URL with
    the email as a parameter and print the response.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
