#!/usr/bin/python3
"""
Module that takes repository name and owner name and list 10 commits
(from most recent to oldest
"""
import sys
import requests

if __name__ == '__main__':

    repo_name, repo_owner = sys.argv[1:3]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    r = requests.get(url)
    if r.status_code == 200:
        for commit in r.json()[:10]:
            print("{}: {}".format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')
            ))
