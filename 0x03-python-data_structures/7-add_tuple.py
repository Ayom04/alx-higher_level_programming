#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        tuple_a = (0, 0)
    elif (len(tuple_a) == 1):
        tuple_a = (tuple_a[0], 0)
    # a1, b1 = tuple_a
    if (len(tuple_b) == 0):
        tuple_b = (0, 0)
    elif (len(tuple_b) == 1):
        tuple_b = (tuple_b[0], 0)
    # a2, b2 = tuple_b
    res1 = tuple_a[0] + tuple_b[0]
    res2 = tuple_a[1] + tuple_b[1]
    tuple_res = (res1, res2)
    return (tuple_res)


add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
