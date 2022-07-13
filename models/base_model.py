#!/usr/bin/env python3
"""
Class Basemodel that define all common attributes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    defines a Basemodel class
    """

    def __init__(self, *arg, **kwargs):
        """initializes the Basemodel"""

        self.id = str(uuid4())
        self.created_at = datetime.isoformat(datetime.now())
        self.updated_at = datetime.isoformat(datetime.now())
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns the print of the basemodel"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """uptade with the current time"""
        models.storage.save()

        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary of the basemodel"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
