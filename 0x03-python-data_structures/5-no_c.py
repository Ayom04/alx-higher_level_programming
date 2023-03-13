#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string

no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
