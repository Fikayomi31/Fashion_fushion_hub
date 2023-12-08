#!/usr/bin/python3
"""Defining the class category"""
from models.base_model import BaseModel


class Category(BaseModel):
    """category class representation
    Attribute:
        category_type (str) - category type
    """
    category_type = ""
