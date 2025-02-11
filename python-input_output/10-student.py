#!/usr/bin/python3
"""
This module defines a class
"""


class Student:
    """
    This class defines an object student
    """
    def __init__(self, first_name, last_name, age):
        """
        This function initializes
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function returns a dict
        Returns:
            dict: dictionnary
        """
        if isinstance(attrs, list) and all(isinstance(
            attr, str) for attr in attrs):
            dict_to_return = {
                i: self.__dict__.get(i) for i in attrs if self.__dict__.get(i)}
        else:
            dict_to_return = self.__dict__

        return dict(sorted(dict_to_return.items(), key=lambda x: len(x[0])))
