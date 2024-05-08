#!/usr/bin/python3
"""Defining a class user"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from os import getenv

storage_type = getenv('FFH_TYPE_STORAGE')

class User(BaseModel):
    """User class representation"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String)
        password = Column(String)
        username = Column(String)
    else:
        email: str = ""
        password: str = ""
        username: str = ""
