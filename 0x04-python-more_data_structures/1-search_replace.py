#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    res = []
    for e in my_list:
        if e == search:
            e = replace
        res.append(e)
    return res
# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)
#
# print(new_list)
# print(my_list)
