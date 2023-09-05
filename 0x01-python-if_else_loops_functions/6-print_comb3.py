#!/usr/bin/python3
for n1 in range(0, 10):
    if n1 == 9:
        break
    for n2 in range(n1, 10):
        if n1 == 8 and n2 == 9:
            print(f"{n1:d}{n2:d}")
            break
        else:
            print(f"{n1:d}{n2:d}", end=", ")
