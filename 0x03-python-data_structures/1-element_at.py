#!/usr/bin/python3
def element_at(my_list, idx):
    for arr in range(len(my_list)):
        if ((idx < 0) or (idx > len(my_list))):
            return (None)
        elif (idx == arr):
            return (my_list[arr])

element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
