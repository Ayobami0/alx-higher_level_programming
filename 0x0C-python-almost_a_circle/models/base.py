#!/usr/bin/python3
"""Base class module"""
import json
import csv
import turtle as t
import random


class Base:
    """Base class with an ID attribute for object identification."""

    __nb_object = 0

    def __init__(self, id=None) -> None:
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
        dummy = None
        if dictionary is None:
            return dummy
        if cls.__name__ == "Base":
            return
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Rectangle Class
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Square Class
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_objs_str = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs],
        )
        with open(filename, "w", encoding="utf-8") as json_f:
            json_f.write(list_objs_str)

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as csvfile:
            csvwriter = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                csvwriter.writerows(
                    [
                        (
                            obj.id,
                            obj.width,
                            obj.height,
                            obj.x,
                            obj.y,
                        )
                        for obj in list_objs
                    ]
                )
            elif cls.__name__ == "Square":
                csvwriter.writerows(
                    [
                        (
                            obj.id,
                            obj.size,
                            obj.x,
                            obj.y,
                        )
                        for obj in list_objs
                    ]
                )

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        results = []
        try:
            with open(filename, "r", encoding="utf-8") as csvfile:
                csvreader = csv.reader(csvfile)
                for rows in csvreader:
                    row_dict = {}
                    if cls.__name__ == "Square":
                        row_dict["id"] = int(rows[0])
                        row_dict["size"] = int(rows[1])
                        row_dict["x"] = int(rows[2])
                        row_dict["y"] = int(rows[3])
                    elif cls.__name__ == "Rectangle":
                        row_dict["id"] = int(rows[0])
                        row_dict["width"] = int(rows[1])
                        row_dict["height"] = int(rows[2])
                        row_dict["x"] = int(rows[3])
                        row_dict["y"] = int(rows[4])
                    if len(row_dict) != 0:
                        results.append(cls.create(**row_dict))
        except Exception:
            pass
        return results

    @staticmethod
    def draw(list_rectangles, list_squares):
        colors = (
            "red",
            "blue",
            "green",
            "yellow",
            "pink",
            "orange",
            "black",
            "indigo",
            "violet",
        )
        for rect in list_rectangles:
            t.speed(2)
            t.color(random.choice(colors))
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.clearscreen()

        for sq in list_squares:
            t.speed(2)
            t.color(random.choice(colors))
            for _ in range(4):
                t.forward(sq.size)
                t.left(90)
            t.clearscreen()
