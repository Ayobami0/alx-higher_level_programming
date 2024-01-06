#!/usr/bin/python3
"""
Featches a link and prints the value of the X-Request-Id
"""
import requests
import sys

url = sys.argv[1]

res = requests.get(url)
header = res.headers
print(header.get("X-Request-Id"))
