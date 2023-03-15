#!/usr/bin/python3

"""Module: base_model
Contans BaseModel class for Airbnb Clone - The console
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class: BaseModel
    Base class for the Airbnb clone
    """

    def __init__(self, id=str(uuid4), c=datetime.now(), u=datetime.now()):
        self.id = id
        self.created_at = c
        self.updated_at = u

    def __str__(self):
        return "[Basemodel] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
