#!/usr/bin/python3
"""
The user Module that contains the User Model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class representation of a User Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
