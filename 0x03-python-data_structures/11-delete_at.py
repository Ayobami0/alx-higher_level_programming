#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) or len(my_list) == 0:
        return my_list
    my_list[:] = [n for n in my_list if n != my_list[idx]]
    return my_list
# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_list = delete_at(my_list, idx)
# print(new_list)
# print(my_list)
