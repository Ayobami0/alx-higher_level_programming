#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_len = [0 for _ in range(list_length)]

    for i in range(max(my_list_2, my_list_1)):
        try:
            new_len[i] = my_list_2 / my_list_1
        except (IndexError, ZeroDivisionError, TypeError) as e:
            if e is IndexError:
                print("out of range")
            elif e is ZeroDivisionError:
                print("division by 0")
            else:
                print("wrong type")
            continue
        finally:
            pass
    return new_len
