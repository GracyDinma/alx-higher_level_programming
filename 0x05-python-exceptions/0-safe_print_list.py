#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    while True:
        try:
            if element < x:
            print(my_list[element], end='')
            element += 1
        else:
            print()
            return element
        except IndexError:
        print()
        return element
