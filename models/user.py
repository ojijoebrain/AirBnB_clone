#!/usr/bin/python3
""" User Model """
from models.base_model import BaseModel


class User(BaseModel):
    """ handles user data """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
