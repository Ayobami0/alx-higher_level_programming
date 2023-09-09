#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    return (
        (tuple_a[0] if len(tuple_a) >= 1 else 0)
        + (tuple_b[0] if len(tuple_b) >= 1 else 0),
        (tuple_a[1] if len(tuple_a) >= 2 else 0)
        + (tuple_b[1] if len(tuple_b) >= 2 else 0)
    )
# print(add_tuple((1, 3), (5, 5)))
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
