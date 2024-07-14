#!/usr/bin/python3
"""Script that sends a POST request to a URL with an email
as a parameter and displays the response body.
"""
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    print(response.read().decode('utf-8'))
