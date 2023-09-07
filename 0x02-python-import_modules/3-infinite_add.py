#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for num in sys.argv[1:]:
        result += int(num)
    print(result)
