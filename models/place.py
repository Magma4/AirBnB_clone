#!/usr/bin/python3
"""this model defines a place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """the place class defines a place and inherits from
    the base class
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *arg, **kwargs):
        """the constructor for the place class"""
        super().__init__(*arg, **kwargs)
