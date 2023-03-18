#!/usr/bin/python3

"""
contains a sub class of BaseModel "User"
"""

from base_model import BaseModel


class User(BaseModel):
    """
    Defines a user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
