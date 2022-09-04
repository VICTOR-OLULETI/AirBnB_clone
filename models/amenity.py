#!/usr/bin/python3
"""Module for Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
	"""Class representing an amenity.

	Attributes:
		name (str): the name of the amenity.
	"""
	
    name = ""