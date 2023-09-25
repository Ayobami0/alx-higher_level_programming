#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                pass
            if i + 1 == x:
                print("")
                return i + 1
        except IndexError as e:
            print(e, end="")
