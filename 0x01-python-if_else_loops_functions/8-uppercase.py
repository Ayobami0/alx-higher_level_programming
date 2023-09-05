#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(
            chr(ord(c) - 32) if ord(c) <= 122 and ord(c) >= 97 else c), end="")
    print("".format())
# uppercase("this is a test")
