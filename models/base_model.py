#!/usr/bin/env python3
"""
Class Basemodel that define all common attributes
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    defines a Basemodel class
    """

    def __init__(self, *arg, **kwargs):

        """initializes the Basemodel"""

        self.id = str(uuid4())
        self.created_at= datetime.isoformat(datetime.now())
        self.updated_at= datetime.isoformat(datetime.now())
        if kwargs:
            for j, c, in kwargs.items():
                if j == "created_at" or j == "updated_at":
                    c = datetime.strptime(c, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, j, c)


    def __str__(self):
        """returns the print of the basemodel"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def __save__(self):
        """uptade with the current time"""
        
        self.updated_at = datetime.isoformat(datetime.now())

    def to_dict(self):
        """return a dictionary of the basemodel"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
