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

    def to_json(self):
        """
        This function returns a dict
        Returns:
            dict: dictionnary
        """
        return self.__dict__
