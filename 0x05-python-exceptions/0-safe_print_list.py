#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for element in range(x):
        try:
            my_list[]
            print(my_list[element])
            count += element
        except IndexError:
            pass
        print()
        return count