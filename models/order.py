#!/usr/bin/python3
""" Defining the class for order"""
from models.base_model import BaseModel
from sqlalchemy import Column,Integer, String, Date, ForeignKey, Float
from os import getenv
from sqlalchemy.sql.schema import ForeignKey
storage_type = getenv('FFH_TYPE_STORAGE')


class Order(BaseModel):
    """Representation of order class
    Attribute:
        user_id (str) - user id
        order_date (str) - datetime
        total_amount (float) - total amount
    """
    __tablename__ = 'orders'
    if storage_type == 'db':
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        order_date = Column(Date)
        total_amount = Column(Float)
    else:        
        user_id = ""
        order_date = ""
        total_amount = 0.0
