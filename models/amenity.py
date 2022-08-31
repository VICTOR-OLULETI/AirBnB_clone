#!/usr/bin/python3
"""This program defines the Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the class definition for Amenity
    which inherits BaseModel
    """

    # Public class attributes
    name = ''

    def __init__(self, *args, **kwargs):
        """Initializing the User class"""
        super().__init__(*args, **kwargs)
