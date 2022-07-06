#!/usr/bin/env python3
#convercion de diccionario a json.json
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorange:
    
    __file_path = "file.json"
    __objects = {} 

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
    
    def save(self):
        pass
        
    def reload(self):
        pass
