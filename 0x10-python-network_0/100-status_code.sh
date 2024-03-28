#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s "$1" -w '%{response_code}' -o /dev/null
