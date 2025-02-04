#!/usr/bin/python3
"""
This module defines a function that checks if the object 
is an instance inherited from a class.
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an
    instance of, or if the object is an instance
    of a class that inherited from, a specified class
    Args:
        obj (): object
        a_class (): class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
