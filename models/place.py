#!/usr/bin/python3
"""This program defines the Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This is the class definition for User
    which inherits BaseModel
    """

    # Public class attributes
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializing the Place class"""
        super().__init__(*args, **kwargs)
