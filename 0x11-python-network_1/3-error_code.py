#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import urllib.error
import sys

url = sys.argv[1]


try:
    with urllib.request.urlopen(url) as res:
        print(res.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('Error code: {}'.format(e.code))
