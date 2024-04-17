#!/usr/bin/python3
""" Module 3-is_kind_of_class
Write a function that returns true when object is an instance.
"""


def is_kind_of_class(obj, a_class):

    """Args:
    - obj: Object that is inherits
    - a_class: class that is inherited from.
    Returns True or False.
    """

    return isinstance(obj, a_class)
