#!/usr/bin/python3
"""Defining the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of the review class
    Attribute:
        user_id (str) - user id
        product_id (str) - product id
        text (str) - comment text

    """
    user_id = ""
    product_id = ""
    text = ""
