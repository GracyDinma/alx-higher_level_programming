#!/usr/bin/python3
"""Module 4-inherits_from.py
Creates a function that returns true if the object is an instance of a class
"""


def inherits_from(obj, a_class):

    """Args:
    obj: object of a class that inherits directly or indirectly.
    a_class: class that object is inherited from

    Returns true or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
