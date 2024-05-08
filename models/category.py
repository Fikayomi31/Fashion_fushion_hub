#!/usr/bin/python3
"""Defining the class category"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from os import getenv

storage_type = getenv('FFH_TYPE_STORAGE')


class Category(BaseModel):
    """category class representation
    Attribute:
        category_type (str) - category type
    """
    __tablename__ = 'categories'
    if storage_type == 'db':
        category_type = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
    else:
        category_type = ""
        description = ""
