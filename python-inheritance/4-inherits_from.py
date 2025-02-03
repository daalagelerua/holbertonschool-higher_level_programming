#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    This function checks if an object is an 
    instance directly or indirectly of a specified class
    Args:
        obj (): object
        a_class (): class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
