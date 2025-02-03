#!/usr/bin/Python3
def is_same_class(obj, a_class):
    """
    This function checks if an object is an exact 
    instance of a class
    Args:
        obj (): object
        a_class (): class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
    