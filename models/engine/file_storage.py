#!/usr/bin/env python3
#convercion de diccionario a json.json
import json
import os
from models.base_model import BaseModel
from models.user import User

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
