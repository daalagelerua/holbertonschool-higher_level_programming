#!/usr/bin/python3
"""
This module defines a class
"""

import pickle


class CustomObject:
    """
    This class define a student
    """

    def __init__(self, name, age, is_student):
        """
        This function
        Args:
            name (str): name of student
            age (int): age of student
            is_student (bool): True or False
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        This function print a display of the object's attributes
        """
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Is Student: ", self.is_student)

    def serialize(self, filename):
        """
        This function serializes data into a json file
        Args:
            filename (str): name of file
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError):
            print("None")

    @classmethod
    def deserialize(cls, filename):
        """
        This function deserializes a json file into data
        Args:
            filename (str): name of file
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError):
            print("None")
