#!/usr/bin/python3
"""This program defines the City"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the class definition for City
    which inherits BaseModel
    """

    # Public class attributes
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """Initializing the User class"""
        super().__init__(*args, **kwargs)
