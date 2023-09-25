#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_len = [0 for _ in range(list_length)]
    for i in range(max(len(my_list_1), len(my_list_2))):
        try:
            new_len[i] = my_list_1[i] / my_list_2[i]
        except (IndexError, ZeroDivisionError, TypeError) as e:
            if isinstance(e, IndexError):
                print("out of range")
            elif isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, TypeError):
                print("wrong type")
        finally:
            continue
    return new_len


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
