#!/usr/bin/python3
"""this is the user module"""

from models.base_model import BaseModel

class User(BaseModel):
    """"the User class is a subclass of the BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *arg, **kwargs):
        """the constructior for a user"""
        super().__init__(*arg, **kwargs)
