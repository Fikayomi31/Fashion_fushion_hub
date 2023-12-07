#!/usr/bin/python3
"""Defining the class category"""
from models.base_model import BaseModel


class Category(BaseModel):
    """category class representation
    Attribute:
        vendor_id (str) - vendor id
        category_type (str) - category type
    """
    vendor_id = ""
    category_type = ""
