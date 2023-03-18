#!/usr/bin/python3

"""
Module: base_model
Contans BaseModel class for Airbnb Clone - The console
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Class: BaseModel
    Base class for the Airbnb clone
    """

    def __init__(self, *args, **kwargs):
        """
        initialization of basemodel
        """
        if (not (kwargs)):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            dt = '%Y-%m-%dT%H:%M:%S.%f'
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'], dt)
            self.updated_at = datetime.strptime(kwargs['updated_at'], dt)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        updated_dict = self.__dict__.copy()
        updated_dict['__class__'] = self.__class__.__name__
        updated_dict['updated_at'] = self.updated_at.isoformat()
        updated_dict['created_at'] = self.created_at.isoformat()
        return updated_dict
