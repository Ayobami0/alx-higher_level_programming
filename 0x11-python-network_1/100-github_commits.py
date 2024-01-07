#!/usr/bin/python3
"""
A Python script that takes a repository name and owner
and uses the GitHub API to get the last 10 commit
"""

if __name__ == "__main__":
    import sys
    import requests

    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]

    headers = {
        "X-GitHub-Api-Version": "2022-11-28",
        "Accept": "application/vnd.github+json",
    }
    res = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(
            repo_owner,
            repo_name,
        ),
        headers=headers,
    )

    jsonBody = res.json()

    try:
        for n in range(10):
            print(
                "{}: {}".format(
                    jsonBody[n].get("sha"),
                    jsonBody[n].get("commit").get("author").get("name"),
                )
            )
    except Exception:
        pass
