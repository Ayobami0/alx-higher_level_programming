#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 != 0:
        print(chr(n - 32), end="")
    else:
        print(chr(n), end="")
