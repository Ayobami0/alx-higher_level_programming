#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print(my_list[i], end="")
        except IndexError:
            pass
    print("")
    return i + 1
