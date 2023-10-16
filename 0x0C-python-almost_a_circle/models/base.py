#!/usr/bin/python3
"""Base class module"""
import json


class Base:
    """Base class with an ID attribute for object identification."""

    __nb_object = 0

    def __init__(self, id) -> None:
        """
        Initialize the Base object with an ID.

        Args:
            id (int): The ID of the object. If None, auto-incremented
                ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_objs_str = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs],
        )
        with open(filename, "w", encoding="utf-8") as json_f:
            json_f.write(list_objs_str)

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        try:
            return json.dumps(list_dictionaries)
        except Exception:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        if len(json_string) == 0 or json_string is None:
            return []
        object_rep = json.loads(json_string)
        return object_rep

    @classmethod
    def create(cls, **dictionary):
        cls.__subclasses__()
        if cls.__name__ == "Base":
            return
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Rectangle Class
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Square Class
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        obj = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                json_string = cls.from_json_string(f.read())
                for o in json_string:
                    obj.append(cls.create(**o))
        except FileNotFoundError:
            pass
        return obj
