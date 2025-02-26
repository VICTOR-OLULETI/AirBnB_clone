#!/usr/bin/python3
"""
This program defines the BaseModel class
"""
from datetime import datetime
from models import storage
# import models
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
        """
        if (not kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        else:
            for key, value in kwargs.items():
                if (key != '__class__'):
                    setattr(self, key, value)
            if kwargs.get("created_at", 0) and type(self.created_at) is str:
                kwargs["created_at"] = datetime.fromisoformat(
                        kwargs["created_at"])
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", 0) and type(self.updated_at) is str:
                kwargs["updated_at"] = datetime.fromisoformat(
                        kwargs["updated_at"])
            else:
                self.updated_at = self.created_at

            if (not kwargs.get("id", 0)):
                self.id = str(uuid.uuid4())
        # self.updated_at = datetime.now()

    """
        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            if (not kwargs.get("id", 0)):
                self.id = str(uuid.uuid4())
            if (kwargs.get("created_at", 0)):
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"])
            else:
                self.created_at = datetime.now()
            if (kwargs.get("updated_at", 0)):
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"])
            else:
                self.updated_at = self.created_at

            if (kwargs.get("__class__", 0)):
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    # Magic Methods
    def __str__(self):
        """String representation of the BaseModel instance"""

        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))
        """
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
        """

    def to_dict(self):
        """Return the representation of the instance BaseModel"""
        dictionary = {}
        dictionary.update(self.__dict__)
        """
        creating = self.created_at
        if (type(creating) is not str):
            creating = self.created_at.isoformat()
        updating = self.updated_at
        if (type(updating) is not str):
            updating = self.updated_at.isoformat()
        dictionary.update({
            '__class__': self.__class__.__name__,
            'created_at': creating, 'updated_at': updating
            })
        """
        dictionary.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return (dictionary)
