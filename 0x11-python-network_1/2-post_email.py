#!/usr/bin/python3
"""
Sends a post request to the url with the email has a query
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode()

    with urllib.request.urlopen(url, data=data) as res:
        print(res.read().decode("utf-8"))
