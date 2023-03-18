#!/usr/bin/python3

"""
contains Review, a subclass of BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines Review
    """

    place_id = ""
    user_id = ""
    text = ""
