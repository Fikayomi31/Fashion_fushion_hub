#!/usr/bin/python3
""" Defining the class for order"""
from models.base_model import BaseModel


class Order(BaseModel):
    """Representation of order class
    Attribute:
        user_id (str) - user id
        order_date (str) - datetime
        total_amount (float) - total amount
    """
    user_id = ""
    order_date = ""
    total_amount = 0.0
