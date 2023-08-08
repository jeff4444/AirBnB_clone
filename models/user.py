#!usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """this creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
