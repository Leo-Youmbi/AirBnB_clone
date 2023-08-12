#!/usr/bin/python3
"""
Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class representation of a Review Model"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
