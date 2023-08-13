#!/usr/bin/python3
"""
BaseModel module
"""
from datetime import datetime
import uuid

import models


class BaseModel:
    """A class representation of a Base Model"""

    def __init__(self, *args, **kwargs):
        """A new instance of the base Model"""
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ('created_at', 'updated_at'):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation"""
        my_dict = self.__dict__.copy()
        for key, value in my_dict.items():
            if key in ("created_at", "updated_at"):
                my_dict[key] = value.isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict
