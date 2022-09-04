#!/usr/bin/python3
"""this model defines a Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """the Review class defines a review and inherits from
    the base class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *arg, **kwargs):
        """the constructor for the state class"""
        super().__init__(*arg, **kwargs)
