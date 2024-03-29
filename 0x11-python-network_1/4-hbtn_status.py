#!/usr/bin/python3
"""
Implements a script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    body = r.text
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
