#!/usr/bin/python3
def remove_char_at(str, n):
    new_arr = ""
    for idx in range(len(str)):
        if idx != n:
            new_arr += str[idx]
    return new_arr
# print(remove_char_at("a test to remove this [a]", 23))
# print(remove_char_at("a test for negative values", -1))
# print(remove_char_at("a test for out of bound index", 100))
