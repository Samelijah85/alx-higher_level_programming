#!/usr/bin/python3
"""
Implements a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    query = sys.argv[1] if len(sys.argv) == 2 else ""

    data = dict(q=query)
    r = requests.post(url, data)
    try:
        json_response = r.json()
        if len(json_response) == 0:
            print('No result')
        else:
            print('[{id}] {name}'.format(**json_response))
    except ValueError:
        print('Not a valid JSON')
