#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys

if __name__ == '__main__':
    url, email = sys.argv[1:3]
    param = {'email': email}
    data = parse.urlencode(param).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        print(body)
