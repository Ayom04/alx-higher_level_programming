#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        s = ""
        for y in x:
            print("{:s}{:d}".format(s, y), end='')
            s = " "
        print()


print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()