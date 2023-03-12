#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list is not None):
        my_list.reverse()
        for arr in range(len(my_list)):
            print("{:d}".format(my_list[arr]))

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)