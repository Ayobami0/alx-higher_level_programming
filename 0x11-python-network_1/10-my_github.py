#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the
GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    headers = {
        "Authorization": "Bearer {}".format(password),
        "X-GitHub-Api-Version": "2022-11-28",
        "Accept": "application/vnd.github+json",
    }
    res = requests.get("https://api.github.com/user", headers=headers)

    jsonBody = res.json()
    print("{}".format(jsonBody.get("id")))
