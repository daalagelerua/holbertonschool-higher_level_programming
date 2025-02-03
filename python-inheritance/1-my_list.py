#!/usr/bin/python3
"""
This module define a class 'MyList'.
This class inherits of 'list' and add a method to
print a sorted version of the list
"""


class MyList(list):
    """
    Class MyList inherits of 'list' and add print_sorted
    Args:
        list (int): list of integer
    """
    def print_sorted(self):
        """
        Shows the list in ascending order without modifying it
        """
        print(sorted(self))
