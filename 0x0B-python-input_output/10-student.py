#!/usr/bin/python3
"""A module module containing a function."""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Convert the Student instance to a dictionary containing
        selected attributes.

        Args:
            attr (list, optional): A list of attribute names to
            include in the dictionary.
                If not provided or set to None, all attributes are included.

        Returns:
            dict: A dictionary containing the selected attributes
            of the instance.
        """
        if attr is None or len(attr) == 0:
            return self.__dict__
        if type(attr) is not list:
            return self.__dict__
        new_dict = {}
        for v in self.__dict__.keys():
            if v in self.__dict__.keys():
                new_dict[v] = self.__dict__[v]
