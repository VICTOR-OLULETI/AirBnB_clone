#!/usr/bin/python3
"""This program defines the User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the class definition for User
    which inherits BaseModel
    """

    # Public class attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initializing the User class"""
        super().__init__(*args, **kwargs)
