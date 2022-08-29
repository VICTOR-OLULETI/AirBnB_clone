#!/usr/bin/python3
"""
This program defines the BaseModel class
"""
from datetime import datetime

class BaseModel:
    """
    This defines the BaseModel class for other classes
    """

    def __init__(self):
        """
        Constructor of BaseModel
        Args:
            id: string
            created_at
            updated_at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
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
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    
    def to_dict(self):
        """Return the representation of the instance BaseModel"""
        self.__dict__.update({
            '__class__':type(b).__name__, 'created_at': datetime.isoformat(self.created_at), 'updated_at': datetime.isoformat(self.updated_at)
            })
         return (self.__dict__)
