#!/usr/bin/python3
"""This program defines the State"""

from models.base_model import BaseModel


class State(BaseModel):
    """This is the class definition for User
    which inherits BaseModel
    """

    # Public class attributes
    name = ''

    def __init__(self, *args, **kwargs):
        """Initializing the User class"""
        super().__init__(*args, **kwargs)
