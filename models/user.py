#!/usr/bin/python3
"""This is Module for User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """class User Public class attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
