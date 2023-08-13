#!/usr/bin/python3
"""File storage engine"""
import json
import os

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

MODELS = [BaseModel, User, Amenity, Place, City, Review, State]


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path: str = "file.json"
    __objects: dict = dict()

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        type(self).__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        path = type(self).__file_path
        my_obj = type(self).__objects
        with open(path, "w", encoding='UTF-8') as f:
            json.dump(
                {key: value.to_dict() for key, value in my_obj.items()},
                f,
                indent=4
            )

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,does nothing.
         If the file doesn’t exist, no exception should be raised)
         """
        path = type(self).__file_path
        if os.path.exists(path):
            with open(path, "r") as f:
                objs = json.load(f)
            for key, value in objs.items():
                for cls in MODELS:
                    if key.split(".")[0] == cls.__name__:
                        obj = cls(**value)
                        self.new(obj)
                        break
