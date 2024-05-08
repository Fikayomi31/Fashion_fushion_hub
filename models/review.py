#!/usr/bin/python3
"""Defining the review class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Date, Integer
from os import getenv

storage_type = getenv('FFH_TYPE_STORAGE')


class Review(BaseModel):
    """Representation of the review class
    Attribute:
        user_id (str) - user id
        product_id (str) - product id
        text (str) - comment text

    """
    if storage_type == 'db':
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        product_id = Column(String(60), ForeignKey('product.id'), nullable=False)
        comment = Column(String(1024))
        review_date = Column(Date)
        rating = Column(Integer)
    else:
        user_id = ""
        product_id = ""
        comment = ""
        review_date = ""
        rating = ""