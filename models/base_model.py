#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    """A class representation of a Base Model"""

    def __init__(self):
        """A new instance of the base Model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """A string representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Saves the changes made"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation"""
        my_dict = self.__dict__
        my_dict["__class__"] = type(self).__name__
        return my_dict
