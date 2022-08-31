#!/usr/bin/python3
"""
This program defines the BaseModel class
"""
from datetime import datetime
from models import storage
#import models
import uuid
"""
from models.engine.file_storage import FileStorage as storage
"""

class BaseModel:
    """
    This defines the BaseModel class for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of BaseModel
        Args:
            id: string
            created_at
            updated_at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        if (kwargs is not None):
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if hasattr(self, key):
                    if key == 'created_at':
                        setattr(self, key, self.created_at)
                    else:
                        setattr(self, key, value)

        self.updated_at = datetime.now()

    # Magic Methods
    def __str__(self):
        """String representation of the BaseModel instance"""
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    
    def save(self):
        """
        Updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    
    def to_dict(self):
        """Return the representation of the instance BaseModel"""
        """
        self.__dict__.update({
            '__class__': 'BaseModel', 'created_at': datetime.isoformat(self.created_at), 'updated_at': datetime.isoformat(self.updated_at)
            })
        """
        creating = self.created_at
        if (type(creating) is not str):
            creating = self.created_at.isoformat()
        updating = self.updated_at
        if (type(updating) is not str):
            updating = self.updated_at.isoformat()
        self.__dict__.update({
            '__class__': 'BaseModel', 'created_at': creating, 'updated_at': updating
            })

        return (self.__dict__)
