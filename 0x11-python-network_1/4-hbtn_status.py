#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    body = res.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
