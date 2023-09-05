#!/usr/bin/python3
for n1 in range(0, 10):
    if n1 == 9:
        break
    for n2 in range(n1 + 1, 10):
        if n1 == n2:
            pass
        if n1 == 8 and n2 == 9:
            print("{:d}{:d}".format(n1, n2))
            break
        else:
            print("{:d}{:d}".format(n1, n2), end=", ")
