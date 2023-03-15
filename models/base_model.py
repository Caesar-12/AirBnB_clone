#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class: BaseModel
    Base class for the Airbnb clone
    """

    def __init__(self, id=str(uuid4()), created_at=datetime.now(), updated_at=datetime.now()):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return "[Basemodel] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
