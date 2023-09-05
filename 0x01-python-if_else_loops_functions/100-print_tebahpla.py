#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 != 0:
        print("{}".format(chr(n - 32)), end="")
    else:
        print("{}".format(chr(n)), end="")
