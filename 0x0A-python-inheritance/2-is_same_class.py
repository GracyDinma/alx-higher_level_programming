#!/usr/bin/python3
""" Module 2-is_same_class
Creates a number that returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):

    """
    Args:
    obj: object to look at
    a_class: class to verify instance of class

    Return True
    """

    return True if type(obj) is a_class else False
