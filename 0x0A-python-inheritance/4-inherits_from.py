#!/usr/bin/python3
"""Module 4-inherits_from.
Creates a function that returns true if the object is an instance
inherited (directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that
    inherited from a_class.

    Args:
    obj: object of a class that inherits directly or indirectly.
    a_class: class that object is inherited from

    Returns True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
