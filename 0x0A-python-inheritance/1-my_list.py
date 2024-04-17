#!/usr/bin/python3
"""Module 1-my_list
Creates a class that inherits from anothr clas.
"""


class MyList(list):
    """The clas MyList inhrits from list."""

    def print_sorted(self):
        """Prints the list sorted in ascending sort."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
