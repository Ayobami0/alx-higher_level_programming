#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{:d}".format(n))
        break
    print("{:02d}".format(n), end=", ")
