#!/usr/bin/python3
"""Featches a link and prints the response"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    body = res.read()
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
    print('\t- utf8 content: {}'.format(body.decode('utf8')))
