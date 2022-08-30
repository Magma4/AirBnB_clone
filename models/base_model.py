#!/usr/bin/env bash
# this is the base model for the airbnb project
""" this model defines all common attributes for other classes"""

import uuid
from datetime import datetime

class BaseModel:
    """this class class defines all
    common attr for all other classes
    """

    def __init__(self):
        """the class constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """the unofficial repr of this class"""
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        """updates 'updated_at' with the currenct time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
