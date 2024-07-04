#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" -o /tmp/curl_output && [ "$(tail -c 3 /tmp/curl_output)" = "200" ] && head -c -3 /tmp/curl_output
