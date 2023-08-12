#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class representation of a User Model"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
