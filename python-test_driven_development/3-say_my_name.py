#!/usr/bin/python3
'''
This module defines a function to print 'My name is'

The function `say_my_name` takes 2 strings as arguments
and returns 
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints the arguments given.

    Parameters:
    first_name: will be the first name of user
    last_name: will be the last name of user

    Returns:


    Raises:
    TypeError: If argument is not a string
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
