#!/usr/bin/python3
"""this model defines a city"""

from models.base_model import BaseModel


class City(BaseModel):
    """the city class defines a city and inherits from
    the base class
    """
    state_id = ""
    name = ""

    def __init__(self, *arg, **kwargs):
        """the constructor for the city class"""
        super().__init__(*arg, **kwargs)
