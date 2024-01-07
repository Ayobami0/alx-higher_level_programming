#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    argv = sys.argv
    if len(argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    if res.headers.get("Content-Type") == "application/json":
        jsonBody = res.json()
        try:
            print("[{}] {}".format(jsonBody["id"], jsonBody["name"]))
        except KeyError:
            print("No result")
    else:
        print("Not a valid JSON")
