#!/usr/bin/python3
"""defines a class user"""
from models.base_model import BaseModel, Base

    class user(BaseModel, Base):
        """Defines user by various attributes"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
