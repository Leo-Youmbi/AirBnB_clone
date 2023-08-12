#!/usr/bin/python3
"""
Amenity Module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representation of a Amenity Model"""
    name: str = ""
