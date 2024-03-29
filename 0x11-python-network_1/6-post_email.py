#!/usr/bin/python3
"""
Implements a script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally
displays the body of the response
"""
import requests
import sys

if __name__ == '__main__':
    url, email = sys.argv[1:3]
    data = dict(email=email)
    r = requests.post(url, data)
    print(r.text)
