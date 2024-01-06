#!/usr/bin/python3
"""
Sends a post request to the url with the email has a query
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
data = {"email": email}

res = requests.post(
    url,
    data=data,
)
print(res.text)
