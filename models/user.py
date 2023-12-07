#!/usr/bin/python3
"""Defining a class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class representation"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
