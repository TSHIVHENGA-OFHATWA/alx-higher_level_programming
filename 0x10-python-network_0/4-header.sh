#!/bin/bash
# Sends a GET request to the URL with a custom header and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
