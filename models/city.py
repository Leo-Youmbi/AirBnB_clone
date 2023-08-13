#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class representation of a City Model"""
    state_id: str = ""
    name: str = ""
