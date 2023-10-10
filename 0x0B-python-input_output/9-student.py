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

    def to_json(self):
        """
        Convert the Student instance to a dictionary containing
        selected attributes.

        Returns:
            dict: A dictionary containing the selected attributes
            of the instance.
        """
        return self.__dict__
