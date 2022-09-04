#!/usr/bin/python3
"""this model defines an amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """the amenity class defines a state and inherits from
    the base class
    """
    name = ""

    def __init__(self, *arg, **kwargs):
        """the constructor for the amenity class"""
        super().__init__(*arg, **kwargs)
