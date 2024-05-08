#!/usr/bin/python3
"""Defining the class of Order items"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from os import getenv

storage_type = getenv('FFH_TYPE_STORAGE')


class OrderItem(BaseModel):
    """Representation of each order item
    Attribute:
        user_id (str) - the user id
        order_id (str) - the order id
        quantity (int) - the quantity purchase
        product_id []- the product id
        subtotal (float) - the subtotal of the item
    """
    __tablename__ = 'order_items'
    if storage_type == 'db':
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        brand_id = Column(String(60), ForeignKey('brand.id'), nullable=False)
        product_id = Column(String(60), ForeignKey('product.id'), nullable=False)
        quantity = Column(Integer)
        subtotal = Column(Float)
    else:    
        user_id = ""
        brand_id = ""
        order_id = ""
        quantity = 0
        product_id = []
        subtotal = 0.0
