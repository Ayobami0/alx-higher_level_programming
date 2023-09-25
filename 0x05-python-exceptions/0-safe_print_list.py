#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print("")
            return i
    print("")
    return i + 1


#
#
# print(safe_print_list([1, "test", 3, 8], x=10))
