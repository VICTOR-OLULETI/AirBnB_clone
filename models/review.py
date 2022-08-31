#!/usr/bin/python3
"""This program defines the Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class definition for User
    which inherits BaseModel
    """

    # Public class attributes
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Initializing the Review class"""
        super().__init__(*args, **kwargs)
